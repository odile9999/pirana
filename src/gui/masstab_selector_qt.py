# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PYTHON\Pirana\src\gui\masstab_selector_qt.ui'
#
# Created: Sun Mar 15 17:01:19 2015
#      by: PyQt4 UI code generator 4.11.3
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


class Ui_DockWidget_MassTabSelector(object):

    def setupUi(self, DockWidget_MassTabSelector):
        DockWidget_MassTabSelector.setObjectName(
            _fromUtf8("DockWidget_MassTabSelector"))
        DockWidget_MassTabSelector.resize(150, 500)
        DockWidget_MassTabSelector.setMinimumSize(QtCore.QSize(150, 300))
        DockWidget_MassTabSelector.setMaximumSize(QtCore.QSize(150, 700))
        DockWidget_MassTabSelector.setFeatures(
            QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetMovable)
        DockWidget_MassTabSelector.setAllowedAreas(
            QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listView_Mass = QtGui.QListView(self.dockWidgetContents)
        self.listView_Mass.setObjectName(_fromUtf8("listView_Mass"))
        self.gridLayout.addWidget(self.listView_Mass, 0, 0, 1, 1)
        self.pushButton_ChangeList = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_ChangeList.setObjectName(
            _fromUtf8("pushButton_ChangeList"))
        self.gridLayout.addWidget(self.pushButton_ChangeList, 1, 0, 1, 1)
        DockWidget_MassTabSelector.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_MassTabSelector)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_MassTabSelector)

    def retranslateUi(self, DockWidget_MassTabSelector):
        DockWidget_MassTabSelector.setWindowTitle(
            _translate("DockWidget_MassTabSelector", "MassTab Selector", None))
        self.pushButton_ChangeList.setText(
            _translate("DockWidget_MassTabSelector", "Change List", None))
