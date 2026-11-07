# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.apps_tab = QWidget()
        self.apps_tab.setObjectName(u"apps_tab")
        self.verticalLayout_2 = QVBoxLayout(self.apps_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ram_button = QPushButton(self.apps_tab)
        self.ram_button.setObjectName(u"ram_button")
        self.ram_button.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.ram_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.all_apps = QRadioButton(self.apps_tab)
        self.all_apps.setObjectName(u"all_apps")

        self.horizontalLayout_2.addWidget(self.all_apps)

        self.system_apps = QRadioButton(self.apps_tab)
        self.system_apps.setObjectName(u"system_apps")

        self.horizontalLayout_2.addWidget(self.system_apps)

        self.off_apps = QRadioButton(self.apps_tab)
        self.off_apps.setObjectName(u"off_apps")

        self.horizontalLayout_2.addWidget(self.off_apps)

        self.user_apps = QRadioButton(self.apps_tab)
        self.user_apps.setObjectName(u"user_apps")

        self.horizontalLayout_2.addWidget(self.user_apps)

        self.search_line = QLineEdit(self.apps_tab)
        self.search_line.setObjectName(u"search_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy)
        self.search_line.setMinimumSize(QSize(0, 0))
        self.search_line.setMaximumSize(QSize(200, 16777215))
        self.search_line.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.search_line)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.apps_list = QListView(self.apps_tab)
        self.apps_list.setObjectName(u"apps_list")
        self.apps_list.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.apps_list)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.install_apk_button = QPushButton(self.apps_tab)
        self.install_apk_button.setObjectName(u"install_apk_button")

        self.horizontalLayout_3.addWidget(self.install_apk_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.delete_apps_button = QPushButton(self.apps_tab)
        self.delete_apps_button.setObjectName(u"delete_apps_button")

        self.horizontalLayout_3.addWidget(self.delete_apps_button)

        self.off_apps_button = QPushButton(self.apps_tab)
        self.off_apps_button.setObjectName(u"off_apps_button")

        self.horizontalLayout_3.addWidget(self.off_apps_button)

        self.on_apps_button = QPushButton(self.apps_tab)
        self.on_apps_button.setObjectName(u"on_apps_button")

        self.horizontalLayout_3.addWidget(self.on_apps_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabs.addTab(self.apps_tab, "")
        self.tools_tab = QWidget()
        self.tools_tab.setObjectName(u"tools_tab")
        self.verticalLayout_3 = QVBoxLayout(self.tools_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.power_off_button = QPushButton(self.tools_tab)
        self.power_off_button.setObjectName(u"power_off_button")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemShutdown))
        self.power_off_button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.power_off_button)

        self.reboot_button = QPushButton(self.tools_tab)
        self.reboot_button.setObjectName(u"reboot_button")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemReboot))
        self.reboot_button.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.reboot_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.mirror_screen_button = QPushButton(self.tools_tab)
        self.mirror_screen_button.setObjectName(u"mirror_screen_button")

        self.verticalLayout_5.addWidget(self.mirror_screen_button)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, 30, -1)
        self.label = QLabel(self.tools_tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.android_model = QLabel(self.tools_tab)
        self.android_model.setObjectName(u"android_model")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.android_model)

        self.label_2 = QLabel(self.tools_tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.android_cpu = QLabel(self.tools_tab)
        self.android_cpu.setObjectName(u"android_cpu")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.android_cpu)

        self.label_3 = QLabel(self.tools_tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.android_memory = QLabel(self.tools_tab)
        self.android_memory.setObjectName(u"android_memory")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.android_memory)

        self.label_4 = QLabel(self.tools_tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.android_version = QLabel(self.tools_tab)
        self.android_version.setObjectName(u"android_version")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.android_version)

        self.label_5 = QLabel(self.tools_tab)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.android_serial_number = QLabel(self.tools_tab)
        self.android_serial_number.setObjectName(u"android_serial_number")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.android_serial_number)

        self.label_6 = QLabel(self.tools_tab)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.android_imei = QLabel(self.tools_tab)
        self.android_imei.setObjectName(u"android_imei")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.android_imei)


        self.horizontalLayout_4.addLayout(self.formLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tabs.addTab(self.tools_tab, "")

        self.horizontalLayout.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HelmDroid QT", None))
        self.ram_button.setText("")
        self.all_apps.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))
        self.system_apps.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0435", None))
        self.off_apps.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u044b\u0435", None))
        self.user_apps.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.install_apk_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 APK", None))
        self.delete_apps_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.off_apps_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.on_apps_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.tabs.setTabText(self.tabs.indexOf(self.apps_tab), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.power_off_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.power_off_button.setText("")
#if QT_CONFIG(tooltip)
        self.reboot_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.reboot_button.setText("")
        self.mirror_screen_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0435\u0440\u043a\u0430\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u044d\u043a\u0440\u0430\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c : ", None))
        self.android_model.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440 : ", None))
        self.android_cpu.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043c\u044f\u0442\u044c : ", None))
        self.android_memory.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f Android : ", None))
        self.android_version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 : ", None))
        self.android_serial_number.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"IMEI : ", None))
        self.android_imei.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tools_tab), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
    # retranslateUi

