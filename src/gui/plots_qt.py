# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PIRENEA\PYTHON\ProjPyDev1\src\gui\plots_qt.ui'
#
# Created: Mon Mar  9 14:05:21 2015
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


class Ui_TabWidget_Plots(object):

    def setupUi(self, TabWidget_Plots):
        TabWidget_Plots.setObjectName(_fromUtf8("TabWidget_Plots"))
        TabWidget_Plots.resize(1400, 900)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            TabWidget_Plots.sizePolicy().hasHeightForWidth())
        TabWidget_Plots.setSizePolicy(sizePolicy)
        self.tab_Signal = QtGui.QWidget()
        self.tab_Signal.setObjectName(_fromUtf8("tab_Signal"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_Signal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        TabWidget_Plots.addTab(self.tab_Signal, _fromUtf8(""))
        self.tab_Spectrum = QtGui.QWidget()
        self.tab_Spectrum.setObjectName(_fromUtf8("tab_Spectrum"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_Spectrum)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        TabWidget_Plots.addTab(self.tab_Spectrum, _fromUtf8(""))
        self.tab_Mass = QtGui.QWidget()
        self.tab_Mass.setObjectName(_fromUtf8("tab_Mass"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_Mass)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        TabWidget_Plots.addTab(self.tab_Mass, _fromUtf8(""))
        self.tab_Peaks = QtGui.QWidget()
        self.tab_Peaks.setObjectName(_fromUtf8("tab_Peaks"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_Peaks)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        TabWidget_Plots.addTab(self.tab_Peaks, _fromUtf8(""))

        self.retranslateUi(TabWidget_Plots)
        TabWidget_Plots.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TabWidget_Plots)

    def retranslateUi(self, TabWidget_Plots):
        TabWidget_Plots.setWindowTitle(
            _translate("TabWidget_Plots", "TabWidget", None))
        TabWidget_Plots.setTabText(TabWidget_Plots.indexOf(
            self.tab_Signal), _translate("TabWidget_Plots", "Signal", None))
        TabWidget_Plots.setTabText(TabWidget_Plots.indexOf(
            self.tab_Spectrum), _translate("TabWidget_Plots", "Spectrum", None))
        TabWidget_Plots.setTabText(TabWidget_Plots.indexOf(
            self.tab_Mass), _translate("TabWidget_Plots", "Mass", None))
        TabWidget_Plots.setTabText(TabWidget_Plots.indexOf(
            self.tab_Peaks), _translate("TabWidget_Plots", "Peaks", None))
