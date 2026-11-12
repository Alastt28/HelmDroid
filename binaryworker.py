import subprocess
import time
import zipfile
import shutil
from pathlib import Path
from PySide6 import QtCore

class BinaryWorker(QtCore.QObject):

    device_status_changed = QtCore.Signal(bool)
    bridge_check = QtCore.Signal(bool)
    bridge_install = QtCore.Signal(bool)
    apps_list_loaded = QtCore.Signal(list)
    ram_text_updated = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.device_connected_status = False

    def check_device(self):
        check_device_text = subprocess.run(
            ["adb", "get-state"],
            capture_output=True, text=True
        )
        self.raw_device_connected_status = "device" in check_device_text.stdout
        if self.device_connected_status != self.raw_device_connected_status:
            self.device_connected_status = self.raw_device_connected_status
            self.device_status_changed.emit(self.device_connected_status)

    def check_bridge(self):
        check_installed_bridge = subprocess.run(
            ["adb", "shell", "pm", "list", "packages", "com.helmdroid.helmbridge"],
            capture_output=True, text=True
        )
        installed = "com.helmdroid.helmbridge" in check_installed_bridge.stdout
        self.bridge_check.emit(installed)

    def install_bridge(self):
        apk_path = Path("bin/HelmBridge.apk").resolve()
        install_apk = subprocess.run(
            ["adb", "install", "-r", "-g", apk_path],
            capture_output=True, text=True
        )
        installed = (install_apk.returncode == 0)
        self.bridge_install.emit(installed)

    def is_system_app(self, app_path: str) -> bool:
        system_app_path = [
            "/system",
            "/system_ext",
            "/product",
            "/vendor",
            "/odm",
            "/oem"
        ]
        result = False

        for system_app in system_app_path:
            if system_app in app_path:
                result = True
                break

        return result

    def disabled_apps(self):
        raw_disabled_apps = subprocess.run(
            ["adb", "shell", "pm", "list", "packages", "-d"],
            capture_output=True, text=True
        )
        disabled_apps_list = []
        lines = raw_disabled_apps.stdout.splitlines()
        for x in lines:
            disabled_app = x.replace("package:", "").strip()
            if disabled_app:
                disabled_apps_list.append(disabled_app)
        return disabled_apps_list
            
    def load_apps_list_fallback(self):
        raw_apps_list = subprocess.run(
            ["adb", "shell", "pm", "list", "packages", "-f"],
            capture_output=True, text=True
        )
            
        self.apps_list = raw_apps_list.stdout.splitlines()
        self.apps_data_fallback = []
        self.disabled_list = self.disabled_apps()

        for x in self.apps_list:
            clean_line = x.replace("package:", "").strip()
            if not clean_line:
                continue

            line_parts = clean_line.rsplit("=", maxsplit=1)
            if len(line_parts) == 2:
                app_path = line_parts[0]
                pkg_name = line_parts[1]
                self.apps_data_fallback.append({
                    "name": pkg_name,
                    "package": pkg_name,
                    "icon_path": "",
                    "app_path": app_path,
                    "is_checked": False,
                    "is_system": self.is_system_app(app_path),
                    "is_disabled": pkg_name in self.disabled_list
                })

        self.apps_list_loaded.emit(self.apps_data_fallback)

    def clear_cache(self):
        local_dir = Path("./cache")
        if local_dir.exists():
            shutil.rmtree(local_dir)
        local_dir.mkdir(parents=True, exist_ok=True)

    def load_apps_list(self):
        self.clear_cache()

        remote_zip = "/sdcard/Android/data/com.helmdroid.helmbridge/files/data.zip"
        local_dir = Path("./cache")
        local_dir.mkdir(parents=True, exist_ok=True)
        local_zip = local_dir / "data.zip"
        json_file = local_dir / "apps.json"
        session_id = str(int(time.time()))

        try:
            subprocess.run(
                ["adb", "shell", "am", "start", "-n", "com.helmdroid.helmbridge/.MainActivity", "-e", "session_id", session_id], 
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
            )

            def bridge_logs(logs_std): 
                logs = subprocess.run(
                    ["adb", "logcat", "-d", "-t", "5000", "HelmBridge:D", "*:S"],
                    capture_output=True, text=True
                )
                return logs_std in logs.stdout

            bridge_start = False
            for log in range(20):
                if bridge_logs(f"Session:{session_id}. Start working"):
                    bridge_start = True
                    break
                time.sleep(0.5)

            if not bridge_start:
                raise Exception("HelmBridge is not responding. Start fallback")

            bridge_stop = False
            for log in range(120):
                if bridge_logs(f"Session:{session_id}. Stop working"):
                    bridge_stop = True
                    break
                time.sleep(0.5)

            if not bridge_stop:
                raise Exception("HelmBridge is not responding. Start fallback")

            subprocess.run(
                ["adb", "pull", remote_zip, str(local_zip)], 
                stdout=subprocess.DEVNULL, check=True
            )

            with zipfile.ZipFile(local_zip, 'r') as zip_ref:
                zip_ref.extractall(local_dir)

            if local_zip.exists():
                local_zip.unlink()

            if json_file.exists():
                import json
                with open(json_file, 'r', encoding='utf-8') as f:
                    raw_json_data = json.load(f)

                self.apps_data_bridge = []
                for item in raw_json_data:
                    icon_filename = item.get("icon", "")
                    icon_path = str(local_dir / "icons" / icon_filename) if icon_filename else ""
                    self.apps_data_bridge.append({
                        "name": item["name"],
                        "package": item["package"],
                        "icon_path": icon_path,
                        "app_path": "",
                        "is_checked": False,
                        "is_system": item["system"],
                        "is_disabled": item["disabled"]
                    })
                self.apps_list_loaded.emit(self.apps_data_bridge)
            else:
                self.load_apps_list_fallback()

        except Exception as e:      
            if local_zip.exists():
                local_zip.unlink()
            self.load_apps_list_fallback()

    def ram_button_text(self):
        if self.device_connected_status:
            raw_ram_text = subprocess.run(
                ["adb", "shell", "cat", "/proc/meminfo"],
                capture_output=True, text=True
            )

            list_ram_text = raw_ram_text.stdout.splitlines()
            mem_total_line = ""
            mem_available_line = ""

            for mem_lines in list_ram_text:
                if "MemTotal:" in mem_lines:
                    mem_total_line = mem_lines
            
                if "MemAvailable:" in mem_lines:
                    mem_available_line = mem_lines

            mem_total_line_parts = mem_total_line.split()
            mem_total = int(mem_total_line_parts[1])

            mem_available_line_parts = mem_available_line.split()
            mem_available = int(mem_available_line_parts[1])
            mem_used = mem_total - mem_available
        
            mem_total_gb = round(mem_total / (1024 * 1024), 1)
            mem_used_gb = round(mem_used / (1024 *1024), 1)

            self.button_text = f"ОЗУ: {mem_used_gb} / {mem_total_gb} ГБ"

            self.ram_text_updated.emit(self.button_text)
        else:
            pass