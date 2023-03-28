# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\dataAnalyzeScience\pythonMain\Class3Team2Api_Scrapy_MongoDB_Project\pyqt5\weather_proje.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_country = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_country.setGeometry(QtCore.QRect(30, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_country.setFont(font)
        self.comboBox_country.setObjectName("comboBox_country")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.comboBox_country.addItem("")
        self.label_city_name = QtWidgets.QLabel(self.centralwidget)
        self.label_city_name.setGeometry(QtCore.QRect(670, 80, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_city_name.setFont(font)
        self.label_city_name.setText("")
        self.label_city_name.setObjectName("label_city_name")
        self.label_appname = QtWidgets.QLabel(self.centralwidget)
        self.label_appname.setGeometry(QtCore.QRect(270, 20, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_appname.setFont(font)
        self.label_appname.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_appname.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_appname.setObjectName("label_appname")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(630, 390, 331, 291))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"background-color: rgb(48, 241, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName("frame")
        self.label_temperature = QtWidgets.QLabel(self.frame)
        self.label_temperature.setGeometry(QtCore.QRect(170, 30, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_temperature.setFont(font)
        self.label_temperature.setText("")
        self.label_temperature.setObjectName("label_temperature")
        self.label_icon_pressure = QtWidgets.QLabel(self.frame)
        self.label_icon_pressure.setGeometry(QtCore.QRect(230, 150, 41, 41))
        self.label_icon_pressure.setStyleSheet("background-image: url(:/newPrefix/Downloads/resilience.png);")
        self.label_icon_pressure.setText("")
        self.label_icon_pressure.setPixmap(QtGui.QPixmap(":/newPrefix/resilience.png"))
        self.label_icon_pressure.setScaledContents(True)
        self.label_icon_pressure.setObjectName("label_icon_pressure")
        self.label_icon_huminity = QtWidgets.QLabel(self.frame)
        self.label_icon_huminity.setGeometry(QtCore.QRect(40, 150, 41, 41))
        self.label_icon_huminity.setStyleSheet("background-image: url(:/newPrefix/humidity (1).png);")
        self.label_icon_huminity.setText("")
        self.label_icon_huminity.setPixmap(QtGui.QPixmap(":/newPrefix/humidity (1).png"))
        self.label_icon_huminity.setScaledContents(True)
        self.label_icon_huminity.setObjectName("label_icon_huminity")
        self.label_icon_wind = QtWidgets.QLabel(self.frame)
        self.label_icon_wind.setGeometry(QtCore.QRect(130, 150, 41, 41))
        self.label_icon_wind.setStyleSheet("background-image: url(:/newPrefix/Downloads/wind.png);")
        self.label_icon_wind.setText("")
        self.label_icon_wind.setPixmap(QtGui.QPixmap(":/newPrefix/wind.png"))
        self.label_icon_wind.setScaledContents(True)
        self.label_icon_wind.setObjectName("label_icon_wind")
        self.label_huminity = QtWidgets.QLabel(self.frame)
        self.label_huminity.setGeometry(QtCore.QRect(40, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_huminity.setFont(font)
        self.label_huminity.setText("")
        self.label_huminity.setObjectName("label_huminity")
        self.label_wind = QtWidgets.QLabel(self.frame)
        self.label_wind.setGeometry(QtCore.QRect(130, 220, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_wind.setFont(font)
        self.label_wind.setText("")
        self.label_wind.setObjectName("label_wind")
        self.label_pressure = QtWidgets.QLabel(self.frame)
        self.label_pressure.setGeometry(QtCore.QRect(230, 220, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_pressure.setFont(font)
        self.label_pressure.setText("")
        self.label_pressure.setObjectName("label_pressure")
        self.label_weather_icon = QtWidgets.QLabel(self.frame)
        self.label_weather_icon.setGeometry(QtCore.QRect(40, 50, 101, 101))
        self.label_weather_icon.setText("")
        self.label_weather_icon.setObjectName("label_weather_icon")
        self.label_icon_situation = QtWidgets.QLabel(self.frame)
        self.label_icon_situation.setGeometry(QtCore.QRect(30, 30, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_icon_situation.setFont(font)
        self.label_icon_situation.setText("")
        self.label_icon_situation.setPixmap(QtGui.QPixmap(":/newPrefix/02d.png"))
        self.label_icon_situation.setObjectName("label_icon_situation")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(620, 160, 351, 201))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(60, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 170, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 115, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_country_info = QtWidgets.QLabel(self.frame_2)
        self.label_country_info.setGeometry(QtCore.QRect(120, 75, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_country_info.setFont(font)
        self.label_country_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_country_info.setText("")
        self.label_country_info.setObjectName("label_country_info")
        self.label_region_info = QtWidgets.QLabel(self.frame_2)
        self.label_region_info.setGeometry(QtCore.QRect(120, 120, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_region_info.setFont(font)
        self.label_region_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_region_info.setText("")
        self.label_region_info.setObjectName("label_region_info")
        self.label_population_info = QtWidgets.QLabel(self.frame_2)
        self.label_population_info.setGeometry(QtCore.QRect(130, 165, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_population_info.setFont(font)
        self.label_population_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_population_info.setText("")
        self.label_population_info.setObjectName("label_population_info")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 20, 91, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/season.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.table_cities = QtWidgets.QTableWidget(self.centralwidget)
        self.table_cities.setGeometry(QtCore.QRect(30, 220, 521, 471))
        self.table_cities.setMinimumSize(QtCore.QSize(521, 0))
        self.table_cities.setMaximumSize(QtCore.QSize(521, 16777215))
        self.table_cities.setObjectName("table_cities")
        self.table_cities.setColumnCount(3)
        self.table_cities.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_cities.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_cities.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_cities.setHorizontalHeaderItem(2, item)
        self.label_update = QtWidgets.QLabel(self.centralwidget)
        self.label_update.setGeometry(QtCore.QRect(720, 810, 201, 31))
        self.label_update.setText("")
        self.label_update.setObjectName("label_update")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(630, 810, 91, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_city = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_city.setGeometry(QtCore.QRect(300, 150, 191, 41))
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 810, 111, 31))
        self.label_7.setObjectName("label_7")
        self.label_source = QtWidgets.QLabel(self.centralwidget)
        self.label_source.setGeometry(QtCore.QRect(180, 810, 191, 31))
        self.label_source.setObjectName("label_source")
        self.Button_find = QtWidgets.QPushButton(self.centralwidget)
        self.Button_find.setGeometry(QtCore.QRect(500, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Button_find.setFont(font)
        self.Button_find.setObjectName("Button_find")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 120, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 197, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(192, 197, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Button_filter = QtWidgets.QPushButton(self.centralwidget)
        self.Button_filter.setGeometry(QtCore.QRect(360, 197, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Button_filter.setFont(font)
        self.Button_filter.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Button_filter.setObjectName("Button_filter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_country.setItemText(0, _translate("MainWindow", "Select A Country"))
        self.comboBox_country.setItemText(1, _translate("MainWindow", "Netherlands"))
        self.comboBox_country.setItemText(2, _translate("MainWindow", "Germany"))
        self.comboBox_country.setItemText(3, _translate("MainWindow", "USA"))
        self.label_appname.setText(_translate("MainWindow", "  WEATHER APP"))
        self.label.setText(_translate("MainWindow", "INFORMATION OF CITY"))
        self.label_2.setText(_translate("MainWindow", "Country:"))
        self.label_4.setText(_translate("MainWindow", "Region:"))
        self.label_3.setText(_translate("MainWindow", "Population:"))
        item = self.table_cities.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "City"))
        item = self.table_cities.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Region"))
        item = self.table_cities.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Population"))
        self.label_6.setText(_translate("MainWindow", "Last update:"))
        self.label_7.setText(_translate("MainWindow", "İnformaiton Source : "))
        self.label_source.setText(_translate("MainWindow", "About Country-region-city"))
        self.Button_find.setText(_translate("MainWindow", "Find"))
        self.label_8.setText(_translate("MainWindow", "City Search"))
        self.Button_filter.setText(_translate("MainWindow", "Filter"))
import test2_rc
import test_rc
