package com.helmdroid.helmbridge

import android.app.Activity
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.drawable.Drawable
import android.os.Bundle
import android.util.Log
import org.json.JSONArray
import org.json.JSONObject
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.FileOutputStream
import java.util.concurrent.Executors
import java.util.zip.ZipEntry
import java.util.zip.ZipOutputStream

class MainActivity : Activity() {
    data class AppData(
        val packageName: String,
        val appName: String,
        val isSystem: Boolean,
        val isDisabled: Boolean
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val baseDir = getExternalFilesDir(null)
        val zipFile = File(baseDir, "data.zip")
        val sessionId = intent.getStringExtra("session_id") ?: "unknown"

        Log.d("HelmBridge", "Session:$sessionId. Start working")
        try {
            val t0 = System.currentTimeMillis()
            val pm = packageManager
            val packages = pm.getInstalledPackages(0)
            val threadPoolSize = Runtime.getRuntime().availableProcessors().coerceAtLeast(2)
            val executor = Executors.newFixedThreadPool(threadPoolSize)
            val results = java.util.Collections.synchronizedList(mutableListOf<AppData>())

            ZipOutputStream(FileOutputStream(zipFile)).use { zos ->
            for (pkg in packages) {
                executor.submit {
                    try {
                        val appInfo = pkg.applicationInfo ?: return@submit
                        val appName = pm.getApplicationLabel(appInfo).toString()
                        val packageName = pkg.packageName
                        val isSystem = (appInfo.flags and android.content.pm.ApplicationInfo.FLAG_SYSTEM) != 0 ||
                                       (appInfo.flags and android.content.pm.ApplicationInfo.FLAG_UPDATED_SYSTEM_APP) != 0
                        val isDisabled = !appInfo.enabled
                        val iconDrawable = appInfo.loadIcon(pm)
                        val bitmap = drawableToBitmap(iconDrawable)
                        val stream = ByteArrayOutputStream()
                        bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream)
                        val iconBytes = stream.toByteArray()
                        bitmap.recycle()
                        stream.close()

                        synchronized(zos) {
                            zos.putNextEntry(ZipEntry("icons/${packageName}.png"))
                            zos.write(iconBytes)
                            zos.closeEntry()
                        }

                        results.add(AppData(packageName, appName, isSystem, isDisabled))
                    } catch (e: Exception) {
                        e.printStackTrace()
                    }
                }
            }

            executor.shutdown()
            while (!executor.isTerminated) {
                Thread.sleep(10)
            }

            val appsJsonArray = JSONArray()
                for (data in results) {
                    val appObj = JSONObject().apply {
                        put("name", data.appName)
                        put("package", data.packageName)
                        put("icon", "${data.packageName}.png")
                        put("system", data.isSystem)
                        put("disabled", data.isDisabled)
                    }
                    appsJsonArray.put(appObj)
                }
                zos.putNextEntry(ZipEntry("apps.json"))
                zos.write(appsJsonArray.toString(2).toByteArray(Charsets.UTF_8))
                zos.closeEntry()
            }
            val totalTime = System.currentTimeMillis() - t0
            Log.d("HelmBridge", "Session:$sessionId. Processing time: $totalTime ms")
        } catch (e: Exception) {
            Log.e("HelmBridge", "Session:$sessionId. Error in main zip process", e)
        }
        Log.d("HelmBridge", "Session:$sessionId. Stop working")
        finish()
        android.os.Process.killProcess(android.os.Process.myPid())
    }

    private fun drawableToBitmap(drawable: Drawable): Bitmap {
        val bitmap = Bitmap.createBitmap(48, 48, Bitmap.Config.ARGB_8888)
        val canvas = Canvas(bitmap)
        drawable.setBounds(0, 0, canvas.width, canvas.height)
        drawable.draw(canvas)
        return bitmap
    }
}