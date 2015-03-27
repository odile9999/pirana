# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PIRENEA\PYTHON\Pirana\src\gui\data_selector_qt.ui'
#
# Created: Mon Mar 23 11:57:07 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


def _fromUtf8(s):
    return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_DockWidget_DataSelector(object):

    def setupUi(self, DockWidget_DataSelector):
        DockWidget_DataSelector.setObjectName(
            _fromUtf8("DockWidget_DataSelector"))
        DockWidget_DataSelector.resize(320, 270)
        DockWidget_DataSelector.setMinimumSize(QtCore.QSize(320, 270))
        DockWidget_DataSelector.setMaximumSize(QtCore.QSize(320, 270))
        DockWidget_DataSelector.setFeatures(
            QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetMovable)
        DockWidget_DataSelector.setAllowedAreas(
            QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.label_Folder = QtGui.QLabel(self.dockWidgetContents)
        self.label_Folder.setGeometry(QtCore.QRect(9, 9, 60, 16))
        self.label_Folder.setMinimumSize(QtCore.QSize(60, 0))
        self.label_Folder.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_Folder.setObjectName(_fromUtf8("label_Folder"))
        self.label_Year = QtGui.QLabel(self.dockWidgetContents)
        self.label_Year.setGeometry(QtCore.QRect(9, 35, 60, 16))
        self.label_Year.setMinimumSize(QtCore.QSize(60, 0))
        self.label_Year.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_Year.setObjectName(_fromUtf8("label_Year"))
        self.label_Month = QtGui.QLabel(self.dockWidgetContents)
        self.label_Month.setGeometry(QtCore.QRect(9, 61, 50, 16))
        self.label_Month.setMinimumSize(QtCore.QSize(50, 0))
        self.label_Month.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_Month.setObjectName(_fromUtf8("label_Month"))
        self.label_Day = QtGui.QLabel(self.dockWidgetContents)
        self.label_Day.setGeometry(QtCore.QRect(9, 87, 50, 16))
        self.label_Day.setMinimumSize(QtCore.QSize(50, 0))
        self.label_Day.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_Day.setObjectName(_fromUtf8("label_Day"))
        self.label_Directory = QtGui.QLabel(self.dockWidgetContents)
        self.label_Directory.setGeometry(QtCore.QRect(9, 113, 44, 16))
        self.label_Directory.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_Directory.setObjectName(_fromUtf8("label_Directory"))
        self.pushButton_StartAnalysis = QtGui.QPushButton(
            self.dockWidgetContents)
        self.pushButton_StartAnalysis.setGeometry(
            QtCore.QRect(90, 210, 130, 23))
        self.pushButton_StartAnalysis.setObjectName(
            _fromUtf8("pushButton_StartAnalysis"))
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(9, 139, 291, 60))
        self.groupBox.setMinimumSize(QtCore.QSize(270, 60))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 60))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_Acquis = QtGui.QLabel(self.groupBox)
        self.label_Acquis.setGeometry(QtCore.QRect(99, 10, 50, 16))
        self.label_Acquis.setObjectName(_fromUtf8("label_Acquis"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(189, 10, 50, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_Number = QtGui.QLabel(self.groupBox)
        self.label_Number.setGeometry(QtCore.QRect(10, 10, 50, 16))
        self.label_Number.setObjectName(_fromUtf8("label_Number"))
        self.comboBox_Number = QtGui.QComboBox(self.groupBox)
        self.comboBox_Number.setGeometry(QtCore.QRect(10, 30, 69, 20))
        self.comboBox_Number.setMaxVisibleItems(100)
        self.comboBox_Number.setObjectName(_fromUtf8("comboBox_Number"))
        self.comboBox_Acquis = QtGui.QComboBox(self.groupBox)
        self.comboBox_Acquis.setGeometry(QtCore.QRect(99, 30, 69, 20))
        self.comboBox_Acquis.setMaxVisibleItems(100)
        self.comboBox_Acquis.setObjectName(_fromUtf8("comboBox_Acquis"))
        self.comboBox_Accum = QtGui.QComboBox(self.groupBox)
        self.comboBox_Accum.setGeometry(QtCore.QRect(189, 30, 69, 20))
        self.comboBox_Accum.setMaxVisibleItems(100)
        self.comboBox_Accum.setObjectName(_fromUtf8("comboBox_Accum"))
        self.lineEdit_Folder = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit_Folder.setGeometry(QtCore.QRect(60, 6, 133, 20))
        self.lineEdit_Folder.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_Folder.setReadOnly(False)
        self.lineEdit_Folder.setObjectName(_fromUtf8("lineEdit_Folder"))
        self.lineEdit_Directory = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit_Directory.setGeometry(QtCore.QRect(60, 110, 250, 20))
        self.lineEdit_Directory.setMinimumSize(QtCore.QSize(240, 0))
        self.lineEdit_Directory.setText(_fromUtf8(""))
        self.lineEdit_Directory.setObjectName(_fromUtf8("lineEdit_Directory"))
        self.comboBox_Day = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_Day.setGeometry(QtCore.QRect(60, 84, 70, 20))
        self.comboBox_Day.setMinimumSize(QtCore.QSize(70, 0))
        self.comboBox_Day.setMaxVisibleItems(31)
        self.comboBox_Day.setObjectName(_fromUtf8("comboBox_Day"))
        self.comboBox_Month = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_Month.setGeometry(QtCore.QRect(60, 58, 70, 20))
        self.comboBox_Month.setMinimumSize(QtCore.QSize(70, 0))
        self.comboBox_Month.setMaxVisibleItems(12)
        self.comboBox_Month.setObjectName(_fromUtf8("comboBox_Month"))
        self.comboBox_Year = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox_Year.setGeometry(QtCore.QRect(60, 32, 70, 20))
        self.comboBox_Year.setMinimumSize(QtCore.QSize(70, 0))
        self.comboBox_Year.setMaxVisibleItems(15)
        self.comboBox_Year.setObjectName(_fromUtf8("comboBox_Year"))
        DockWidget_DataSelector.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_DataSelector)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_DataSelector)

    def retranslateUi(self, DockWidget_DataSelector):
        DockWidget_DataSelector.setWindowTitle(
            _translate("DockWidget_DataSelector", "Data Selector", None))
        self.label_Folder.setText(
            _translate("DockWidget_DataSelector", "Root", None))
        self.label_Year.setText(
            _translate("DockWidget_DataSelector", "Year", None))
        self.label_Month.setText(
            _translate("DockWidget_DataSelector", "Month", None))
        self.label_Day.setText(
            _translate("DockWidget_DataSelector", "Day", None))
        self.label_Directory.setText(
            _translate("DockWidget_DataSelector", "Folder", None))
        self.pushButton_StartAnalysis.setText(
            _translate("DockWidget_DataSelector", "Start Analysis", None))
        self.label_Acquis.setText(
            _translate("DockWidget_DataSelector", "Acquis", None))
        self.label_3.setText(
            _translate("DockWidget_DataSelector", "Accum", None))
        self.label_Number.setText(
            _translate("DockWidget_DataSelector", "Number", None))
        self.lineEdit_Folder.setText(
            _translate("DockWidget_DataSelector", "D:\\PIRENEA_manips", None))
