import sys, subprocess, os
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtWidgets import QMessageBox
from ui_form import Ui_MainWindow
from binaryworker import BinaryWorker
from appsmodel import AppsModel
from appsproxymodel import AppsProxyModel

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabs.setCurrentIndex(0)

        self.worker_thread = QtCore.QThread()
        self.worker = BinaryWorker()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.worker.device_status_changed.connect(self.device_status_changed_gui)
        self.worker.apps_list_loaded.connect(self.load_apps_list_gui)
        self.worker.ram_text_updated.connect(self.ram_button_text_gui)
        self.worker.bridge_check.connect(self.bridge_check_gui)
        self.worker.bridge_install.connect(self.bridge_install_gui)

        self.apps_model = AppsModel()
        self.ui.apps_list.setModel(self.apps_model)

        self.proxy_model = AppsProxyModel(self)
        self.proxy_model.setSourceModel(self.apps_model)
        self.proxy_model.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.apps_list.setModel(self.proxy_model)

        self.ui.search_line.textChanged.connect(self.proxy_model.setFilterFixedString)

        self.ui.all_apps.clicked.connect(lambda: self.proxy_model.set_filter_mode("all"))
        self.ui.system_apps.clicked.connect(lambda: self.proxy_model.set_filter_mode("system"))
        self.ui.user_apps.clicked.connect(lambda: self.proxy_model.set_filter_mode("user"))
        self.ui.off_apps.clicked.connect(lambda: self.proxy_model.set_filter_mode("disabled"))

        self.ui.all_apps.setChecked(True)

        #TODO Перенеси в appsmodel и по хорошему убери хардкод размера иконок, чё за бред?
        self.ui.apps_list.setIconSize(QtCore.QSize(48, 48))

        self.timer = QtCore.QTimer(self)
        self.timer.start(500)
        self.timer.timeout.connect(self.worker.ram_button_text)
        self.timer.timeout.connect(self.worker.check_device)

        # Кнопки
        self.ui.ram_button.clicked.connect(self.ram_window_gui)
        self.ui.install_apk_button.clicked.connect(self.install_apk)
        self.ui.delete_apps_button.clicked.connect(self.delete_apps_gui)
        self.ui.off_apps_button.clicked.connect(self.off_apps_gui)
        self.ui.on_apps_button.clicked.connect(self.on_apps_gui)
        self.ui.mirror_screen_button.clicked.connect(self.mirror_screen)

        # Объединение всех кнопок в один список для удобства
        self.all_buttons = [
            self.ui.ram_button,
            self.ui.install_apk_button,
            self.ui.delete_apps_button,
            self.ui.off_apps_button,
            self.ui.on_apps_button,
            self.ui.mirror_screen_button
        ]

        # Кнопки изначально выключены
        for button in self.all_buttons: 
            button.setEnabled(False)

    def device_status_changed_gui(self, device_connect_status: bool):
        if device_connect_status:
            QtCore.QTimer.singleShot(0, self.worker.check_bridge)
        else:
            self.apps_model.set_apps([])
            self.ui.ram_button.setText("")
        for button in self.all_buttons:
            button.setEnabled(device_connect_status)

    def bridge_check_gui(self, installed: bool):
        if installed:
            self.apps_model.set_apps([])
            QtCore.QTimer.singleShot(0, self.worker.load_apps_list)
        else:
            reply = QMessageBox.question(
                self,
                "Установка HelmBridge",
                "Для отображения иконок и названий приложений рекомендуется установить HelmBridge.\nУстановить сейчас?",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                QtCore.QTimer.singleShot(0, self.worker.install_bridge)
            else:
                self.apps_model.set_apps([])
                QtCore.QTimer.singleShot(0, self.worker.load_apps_list_fallback)

    def bridge_install_gui(self, installed: bool):
        if installed:
            QtCore.QTimer.singleShot(0, self.worker.load_apps_list)
        else:
            QMessageBox.critical(
                self,
                "Ошибка установки",
                "Не удалось установить HelmBridge на устройство.\nСписок будет загружен без иконок и названий."
            )
            QtCore.QTimer.singleShot(0, self.worker.load_apps_list_fallback)        


    def load_apps_list_gui(self, apps_data: list):
        self.apps_model.set_apps(apps_data)

    def get_checked_packages(self):
        checked_packages = []
        for app in self.apps_model._apps:
            if app["is_checked"] == True:
                checked_packages.append(app["package"])
        return checked_packages

    def ram_button_text_gui(self, button_text: str):
        self.ui.ram_button.setText(button_text)

    def ram_window_gui(self):
        pass

    def delete_apps_gui(self):
        pass

    def off_apps_gui(self):
        pass

    def on_apps_gui(self):
        pass

    def install_apk(self):
        apk_list = QFileDialog.getOpenFileNames(self,
        "Выбор APK", "", ".apk (*.apk)")[0]
        installed_list = []
        error_list = []
        if apk_list:
            for apk_path in apk_list:
                result = subprocess.run(
                    ["adb", "install", apk_path], 
                    capture_output=True, text=True
                )

                file_apk_name = os.path.basename(apk_path)
                if "Success" in result.stdout:
                    installed_list.append(file_apk_name)
                else:
                    error_list.append(f"{file_apk_name}: {result.stderr}")
            if installed_list:
                QMessageBox.information(self,
                    "Установка APK",
                    f"Приложения {', '.join(installed_list)} установлены"
                )
            if error_list:
                QMessageBox.critical(self,
                    "Установка APK",
                    f"Ошибка установки приложений: {', '.join(error_list)}"
                )
    def mirror_screen(self):
        try:
            subprocess.Popen(["scrcpy"])
        except FileNotFoundError:
            QMessageBox.warning(
                self, 
                "Ошибка", 
                "Утилита scrcpy не найдена в системе. Убедитесь, что она установлена."
            )

    def closeEvent(self, event):
        self.apps_model.set_apps([])
        self.worker_thread.quit()
        self.worker_thread.wait()
        self.worker.clear_cache()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
