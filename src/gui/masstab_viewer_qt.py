# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PIRENEA\PYTHON\Pirana\src\gui\masstab_viewer_qt.ui'
#
# Created: Thu Mar 19 10:03:04 2015
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


class Ui_DockWidget_MassTabViewer(object):

    def setupUi(self, DockWidget_MassTabViewer):
        DockWidget_MassTabViewer.setObjectName(
            _fromUtf8("DockWidget_MassTabViewer"))
        DockWidget_MassTabViewer.resize(1050, 186)
        DockWidget_MassTabViewer.setMinimumSize(QtCore.QSize(1050, 186))
        DockWidget_MassTabViewer.setMaximumSize(QtCore.QSize(1050, 400))
        DockWidget_MassTabViewer.setFeatures(
            QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetMovable)
        DockWidget_MassTabViewer.setAllowedAreas(
            QtCore.Qt.BottomDockWidgetArea | QtCore.Qt.TopDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plainTextEdit_Viewer = QtGui.QPlainTextEdit(
            self.dockWidgetContents)
        self.plainTextEdit_Viewer.setStyleSheet(
            _fromUtf8("font: 8pt \"Courier\";"))
        self.plainTextEdit_Viewer.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit_Viewer.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Viewer.setObjectName(
            _fromUtf8("plainTextEdit_Viewer"))
        self.horizontalLayout.addWidget(self.plainTextEdit_Viewer)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_Clear = QtGui.QPushButton(self.groupBox)
        self.pushButton_Clear.setObjectName(_fromUtf8("pushButton_Clear"))
        self.verticalLayout.addWidget(self.pushButton_Clear)
        self.label_Accuracy = QtGui.QLabel(self.groupBox)
        self.label_Accuracy.setObjectName(_fromUtf8("label_Accuracy"))
        self.verticalLayout.addWidget(self.label_Accuracy)
        self.doubleSpinBox_Accuracy = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Accuracy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_Accuracy.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_Accuracy.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_Accuracy.setMaximum(1.0)
        self.doubleSpinBox_Accuracy.setSingleStep(0.1)
        self.doubleSpinBox_Accuracy.setProperty("value", 0.2)
        self.doubleSpinBox_Accuracy.setObjectName(
            _fromUtf8("doubleSpinBox_Accuracy"))
        self.verticalLayout.addWidget(self.doubleSpinBox_Accuracy)
        self.pushButton_Automatic = QtGui.QPushButton(self.groupBox)
        self.pushButton_Automatic.setEnabled(False)
        self.pushButton_Automatic.setObjectName(
            _fromUtf8("pushButton_Automatic"))
        self.verticalLayout.addWidget(self.pushButton_Automatic)
        self.pushButton_Write = QtGui.QPushButton(self.groupBox)
        self.pushButton_Write.setEnabled(False)
        self.pushButton_Write.setObjectName(_fromUtf8("pushButton_Write"))
        self.verticalLayout.addWidget(self.pushButton_Write)
        self.horizontalLayout.addWidget(self.groupBox)
        DockWidget_MassTabViewer.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_MassTabViewer)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_MassTabViewer)

    def retranslateUi(self, DockWidget_MassTabViewer):
        DockWidget_MassTabViewer.setWindowTitle(
            _translate("DockWidget_MassTabViewer", "MassTab Viewer", None))
        self.pushButton_Clear.setText(
            _translate("DockWidget_MassTabViewer", "Clear", None))
        self.label_Accuracy.setText(
            _translate("DockWidget_MassTabViewer", "Accuracy", None))
        self.pushButton_Automatic.setText(
            _translate("DockWidget_MassTabViewer", "Automatic Fill", None))
        self.pushButton_Write.setText(
            _translate("DockWidget_MassTabViewer", "Write to File...", None))
