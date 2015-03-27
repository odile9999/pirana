# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PYTHON\ProjPyDev1\src\gui\sequence_qt.ui'
#
# Created: Mon Mar  2 21:26:23 2015
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

class Ui_DockWidget_Sequence(object):
    def setupUi(self, DockWidget_Sequence):
        DockWidget_Sequence.setObjectName(_fromUtf8("DockWidget_Sequence"))
        DockWidget_Sequence.resize(340, 200)
        DockWidget_Sequence.setMinimumSize(QtCore.QSize(340, 200))
        DockWidget_Sequence.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        DockWidget_Sequence.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView_Sequence = QtGui.QTableView(self.dockWidgetContents)
        self.tableView_Sequence.setObjectName(_fromUtf8("tableView_Sequence"))
        self.verticalLayout.addWidget(self.tableView_Sequence)
        DockWidget_Sequence.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_Sequence)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_Sequence)

    def retranslateUi(self, DockWidget_Sequence):
        DockWidget_Sequence.setWindowTitle(_translate("DockWidget_Sequence", "Sequence", None))

