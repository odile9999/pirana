# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\S.O.F.T.S\PIRENEA\PYTHON\Pirana\src\gui\analysis_qt.ui'
#
# Created: Mon Mar 23 17:31:46 2015
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


class Ui_DockWidget_Analysis(object):

    def setupUi(self, DockWidget_Analysis):
        DockWidget_Analysis.setObjectName(_fromUtf8("DockWidget_Analysis"))
        DockWidget_Analysis.resize(1050, 200)
        DockWidget_Analysis.setMinimumSize(QtCore.QSize(1050, 200))
        DockWidget_Analysis.setMaximumSize(QtCore.QSize(1050, 200))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.groupBox_Signal = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_Signal.setGeometry(QtCore.QRect(10, 30, 311, 131))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox_Signal.setFont(font)
        self.groupBox_Signal.setObjectName(_fromUtf8("groupBox_Signal"))
        self.label_ExcitTruncate = QtGui.QLabel(self.groupBox_Signal)
        self.label_ExcitTruncate.setGeometry(QtCore.QRect(160, 10, 70, 16))
        self.label_ExcitTruncate.setObjectName(
            _fromUtf8("label_ExcitTruncate"))
        self.label_EndTruncate = QtGui.QLabel(self.groupBox_Signal)
        self.label_EndTruncate.setGeometry(QtCore.QRect(240, 10, 70, 16))
        self.label_EndTruncate.setObjectName(_fromUtf8("label_EndTruncate"))
        self.label_Step = QtGui.QLabel(self.groupBox_Signal)
        self.label_Step.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_Step.setObjectName(_fromUtf8("label_Step"))
        self.label_Points = QtGui.QLabel(self.groupBox_Signal)
        self.label_Points.setGeometry(QtCore.QRect(10, 60, 65, 16))
        self.label_Points.setObjectName(_fromUtf8("label_Points"))
        self.spinBox_StartSignal = QtGui.QSpinBox(self.groupBox_Signal)
        self.spinBox_StartSignal.setGeometry(QtCore.QRect(160, 60, 60, 20))
        self.spinBox_StartSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_StartSignal.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_StartSignal.setMaximum(10000000)
        self.spinBox_StartSignal.setProperty("value", 0)
        self.spinBox_StartSignal.setObjectName(
            _fromUtf8("spinBox_StartSignal"))
        self.spinBox_DefEndSignal = QtGui.QSpinBox(self.groupBox_Signal)
        self.spinBox_DefEndSignal.setEnabled(False)
        self.spinBox_DefEndSignal.setGeometry(QtCore.QRect(240, 30, 60, 20))
        self.spinBox_DefEndSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_DefEndSignal.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_DefEndSignal.setMaximum(10000000)
        self.spinBox_DefEndSignal.setObjectName(
            _fromUtf8("spinBox_DefEndSignal"))
        self.spinBox_EndSignal = QtGui.QSpinBox(self.groupBox_Signal)
        self.spinBox_EndSignal.setGeometry(QtCore.QRect(240, 60, 60, 20))
        self.spinBox_EndSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_EndSignal.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_EndSignal.setMaximum(10000000)
        self.spinBox_EndSignal.setObjectName(_fromUtf8("spinBox_EndSignal"))
        self.spinBox_DefStartSignal = QtGui.QSpinBox(self.groupBox_Signal)
        self.spinBox_DefStartSignal.setEnabled(False)
        self.spinBox_DefStartSignal.setGeometry(QtCore.QRect(160, 30, 60, 20))
        self.spinBox_DefStartSignal.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_DefStartSignal.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_DefStartSignal.setMaximum(10000000)
        self.spinBox_DefStartSignal.setObjectName(
            _fromUtf8("spinBox_DefStartSignal"))
        self.doubleSpinBox_Step = QtGui.QDoubleSpinBox(self.groupBox_Signal)
        self.doubleSpinBox_Step.setEnabled(False)
        self.doubleSpinBox_Step.setGeometry(QtCore.QRect(80, 30, 60, 20))
        self.doubleSpinBox_Step.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_Step.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_Step.setDecimals(3)
        self.doubleSpinBox_Step.setMaximum(10.0)
        self.doubleSpinBox_Step.setObjectName(_fromUtf8("doubleSpinBox_Step"))
        self.spinBox_Points = QtGui.QSpinBox(self.groupBox_Signal)
        self.spinBox_Points.setEnabled(False)
        self.spinBox_Points.setGeometry(QtCore.QRect(80, 60, 60, 20))
        self.spinBox_Points.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_Points.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_Points.setMaximum(100000000)
        self.spinBox_Points.setProperty("value", 0)
        self.spinBox_Points.setObjectName(_fromUtf8("spinBox_Points"))
        self.checkBox_Hann = QtGui.QCheckBox(self.groupBox_Signal)
        self.checkBox_Hann.setGeometry(QtCore.QRect(10, 95, 60, 17))
        self.checkBox_Hann.setChecked(True)
        self.checkBox_Hann.setObjectName(_fromUtf8("checkBox_Hann"))
        self.buttonGroup_Hann = QtGui.QButtonGroup(DockWidget_Analysis)
        self.buttonGroup_Hann.setObjectName(_fromUtf8("buttonGroup_Hann"))
        self.buttonGroup_Hann.addButton(self.checkBox_Hann)
        self.checkBox_ZeroFill = QtGui.QCheckBox(self.groupBox_Signal)
        self.checkBox_ZeroFill.setGeometry(QtCore.QRect(230, 90, 80, 17))
        self.checkBox_ZeroFill.setChecked(False)
        self.checkBox_ZeroFill.setObjectName(_fromUtf8("checkBox_ZeroFill"))
        self.buttonGroup_Zero = QtGui.QButtonGroup(DockWidget_Analysis)
        self.buttonGroup_Zero.setObjectName(_fromUtf8("buttonGroup_Zero"))
        self.buttonGroup_Zero.addButton(self.checkBox_ZeroFill)
        self.checkBox_HalfHann = QtGui.QCheckBox(self.groupBox_Signal)
        self.checkBox_HalfHann.setGeometry(QtCore.QRect(60, 95, 80, 17))
        self.checkBox_HalfHann.setChecked(False)
        self.checkBox_HalfHann.setObjectName(_fromUtf8("checkBox_HalfHann"))
        self.buttonGroup_Hann.addButton(self.checkBox_HalfHann)
        self.checkBox_ZeroFillTwice = QtGui.QCheckBox(self.groupBox_Signal)
        self.checkBox_ZeroFillTwice.setGeometry(QtCore.QRect(230, 110, 90, 17))
        self.checkBox_ZeroFillTwice.setChecked(True)
        self.checkBox_ZeroFillTwice.setObjectName(
            _fromUtf8("checkBox_ZeroFillTwice"))
        self.buttonGroup_Zero.addButton(self.checkBox_ZeroFillTwice)
        self.checkBox_NoZero = QtGui.QCheckBox(self.groupBox_Signal)
        self.checkBox_NoZero.setGeometry(QtCore.QRect(150, 100, 70, 17))
        self.checkBox_NoZero.setChecked(False)
        self.checkBox_NoZero.setObjectName(_fromUtf8("checkBox_NoZero"))
        self.buttonGroup_Zero.addButton(self.checkBox_NoZero)
        self.groupBox_Mass = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_Mass.setGeometry(QtCore.QRect(340, 10, 340, 150))
        self.groupBox_Mass.setObjectName(_fromUtf8("groupBox_Mass"))
        self.label_RefMass = QtGui.QLabel(self.groupBox_Mass)
        self.label_RefMass.setGeometry(QtCore.QRect(10, 31, 95, 16))
        self.label_RefMass.setObjectName(_fromUtf8("label_RefMass"))
        self.label_CycloFreq = QtGui.QLabel(self.groupBox_Mass)
        self.label_CycloFreq.setGeometry(QtCore.QRect(10, 60, 95, 16))
        self.label_CycloFreq.setObjectName(_fromUtf8("label_CycloFreq"))
        self.label_MagFreq = QtGui.QLabel(self.groupBox_Mass)
        self.label_MagFreq.setGeometry(QtCore.QRect(10, 90, 95, 16))
        self.label_MagFreq.setObjectName(_fromUtf8("label_MagFreq"))
        self.label_PlotStartMass = QtGui.QLabel(self.groupBox_Mass)
        self.label_PlotStartMass.setGeometry(QtCore.QRect(10, 120, 95, 16))
        self.label_PlotStartMass.setObjectName(
            _fromUtf8("label_PlotStartMass"))
        self.checkBox_Hold = QtGui.QCheckBox(self.groupBox_Mass)
        self.checkBox_Hold.setGeometry(QtCore.QRect(260, 120, 70, 17))
        self.checkBox_Hold.setObjectName(_fromUtf8("checkBox_Hold"))
        self.doubleSpinBox_RefMass = QtGui.QDoubleSpinBox(self.groupBox_Mass)
        self.doubleSpinBox_RefMass.setGeometry(QtCore.QRect(110, 30, 70, 20))
        self.doubleSpinBox_RefMass.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_RefMass.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_RefMass.setDecimals(5)
        self.doubleSpinBox_RefMass.setMaximum(1000.0)
        self.doubleSpinBox_RefMass.setProperty("value", 303.0939)
        self.doubleSpinBox_RefMass.setObjectName(
            _fromUtf8("doubleSpinBox_RefMass"))
        self.doubleSpinBox_CycloFreq = QtGui.QDoubleSpinBox(self.groupBox_Mass)
        self.doubleSpinBox_CycloFreq.setGeometry(QtCore.QRect(110, 60, 70, 20))
        self.doubleSpinBox_CycloFreq.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_CycloFreq.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_CycloFreq.setDecimals(5)
        self.doubleSpinBox_CycloFreq.setMaximum(1000.0)
        self.doubleSpinBox_CycloFreq.setProperty("value", 255.727)
        self.doubleSpinBox_CycloFreq.setObjectName(
            _fromUtf8("doubleSpinBox_CycloFreq"))
        self.doubleSpinBox_MagFreq = QtGui.QDoubleSpinBox(self.groupBox_Mass)
        self.doubleSpinBox_MagFreq.setGeometry(QtCore.QRect(110, 90, 70, 20))
        self.doubleSpinBox_MagFreq.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_MagFreq.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_MagFreq.setDecimals(5)
        self.doubleSpinBox_MagFreq.setMaximum(100.0)
        self.doubleSpinBox_MagFreq.setProperty("value", 0.001)
        self.doubleSpinBox_MagFreq.setObjectName(
            _fromUtf8("doubleSpinBox_MagFreq"))
        self.doubleSpinBox_PlotMassX1 = QtGui.QDoubleSpinBox(
            self.groupBox_Mass)
        self.doubleSpinBox_PlotMassX1.setGeometry(
            QtCore.QRect(110, 120, 60, 20))
        self.doubleSpinBox_PlotMassX1.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PlotMassX1.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PlotMassX1.setDecimals(1)
        self.doubleSpinBox_PlotMassX1.setMaximum(1000.0)
        self.doubleSpinBox_PlotMassX1.setProperty("value", 10.0)
        self.doubleSpinBox_PlotMassX1.setObjectName(
            _fromUtf8("doubleSpinBox_PlotMassX1"))
        self.doubleSpinBox_PlotMassX2 = QtGui.QDoubleSpinBox(
            self.groupBox_Mass)
        self.doubleSpinBox_PlotMassX2.setGeometry(
            QtCore.QRect(180, 120, 60, 20))
        self.doubleSpinBox_PlotMassX2.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PlotMassX2.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PlotMassX2.setDecimals(1)
        self.doubleSpinBox_PlotMassX2.setMaximum(3000.0)
        self.doubleSpinBox_PlotMassX2.setProperty("value", 600.0)
        self.doubleSpinBox_PlotMassX2.setObjectName(
            _fromUtf8("doubleSpinBox_PlotMassX2"))
        self.groupBox_Peak = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox_Peak.setGeometry(QtCore.QRect(700, 40, 340, 81))
        self.groupBox_Peak.setObjectName(_fromUtf8("groupBox_Peak"))
        self.label_PeakHeight = QtGui.QLabel(self.groupBox_Peak)
        self.label_PeakHeight.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_PeakHeight.setObjectName(_fromUtf8("label_PeakHeight"))
        self.label_PeakDistance = QtGui.QLabel(self.groupBox_Peak)
        self.label_PeakDistance.setGeometry(QtCore.QRect(10, 55, 81, 16))
        self.label_PeakDistance.setObjectName(_fromUtf8("label_PeakDistance"))
        self.label_StartMass = QtGui.QLabel(self.groupBox_Peak)
        self.label_StartMass.setGeometry(QtCore.QRect(190, 30, 70, 16))
        self.label_StartMass.setObjectName(_fromUtf8("label_StartMass"))
        self.label_EndMass = QtGui.QLabel(self.groupBox_Peak)
        self.label_EndMass.setGeometry(QtCore.QRect(190, 55, 70, 16))
        self.label_EndMass.setObjectName(_fromUtf8("label_EndMass"))
        self.doubleSpinBox_PeakHeight = QtGui.QDoubleSpinBox(
            self.groupBox_Peak)
        self.doubleSpinBox_PeakHeight.setGeometry(
            QtCore.QRect(100, 30, 60, 20))
        self.doubleSpinBox_PeakHeight.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_PeakHeight.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_PeakHeight.setDecimals(3)
        self.doubleSpinBox_PeakHeight.setObjectName(
            _fromUtf8("doubleSpinBox_PeakHeight"))
        self.spinBox_PeakDistance = QtGui.QSpinBox(self.groupBox_Peak)
        self.spinBox_PeakDistance.setGeometry(QtCore.QRect(100, 55, 30, 20))
        self.spinBox_PeakDistance.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_PeakDistance.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_PeakDistance.setMaximum(10000)
        self.spinBox_PeakDistance.setProperty("value", 0)
        self.spinBox_PeakDistance.setObjectName(
            _fromUtf8("spinBox_PeakDistance"))
        self.doubleSpinBox_StartMass = QtGui.QDoubleSpinBox(self.groupBox_Peak)
        self.doubleSpinBox_StartMass.setGeometry(QtCore.QRect(260, 30, 60, 20))
        self.doubleSpinBox_StartMass.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_StartMass.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_StartMass.setDecimals(1)
        self.doubleSpinBox_StartMass.setMaximum(1000.0)
        self.doubleSpinBox_StartMass.setObjectName(
            _fromUtf8("doubleSpinBox_StartMass"))
        self.doubleSpinBox_EndMass = QtGui.QDoubleSpinBox(self.groupBox_Peak)
        self.doubleSpinBox_EndMass.setGeometry(QtCore.QRect(260, 55, 60, 20))
        self.doubleSpinBox_EndMass.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBox_EndMass.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_EndMass.setDecimals(1)
        self.doubleSpinBox_EndMass.setMaximum(1000.0)
        self.doubleSpinBox_EndMass.setObjectName(
            _fromUtf8("doubleSpinBox_EndMass"))
        self.spinBox_PeakDistanceFound = QtGui.QSpinBox(self.groupBox_Peak)
        self.spinBox_PeakDistanceFound.setEnabled(False)
        self.spinBox_PeakDistanceFound.setGeometry(
            QtCore.QRect(135, 55, 30, 20))
        self.spinBox_PeakDistanceFound.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.spinBox_PeakDistanceFound.setButtonSymbols(
            QtGui.QAbstractSpinBox.NoButtons)
        self.spinBox_PeakDistanceFound.setMaximum(10000)
        self.spinBox_PeakDistanceFound.setProperty("value", 0)
        self.spinBox_PeakDistanceFound.setObjectName(
            _fromUtf8("spinBox_PeakDistanceFound"))
        self.pushButton_UpdatePlots = QtGui.QPushButton(
            self.dockWidgetContents)
        self.pushButton_UpdatePlots.setEnabled(False)
        self.pushButton_UpdatePlots.setGeometry(
            QtCore.QRect(920, 130, 110, 23))
        self.pushButton_UpdatePlots.setMaximumSize(
            QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_UpdatePlots.setFont(font)
        self.pushButton_UpdatePlots.setObjectName(
            _fromUtf8("pushButton_UpdatePlots"))
        self.lineEdit_File = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit_File.setEnabled(False)
        self.lineEdit_File.setGeometry(QtCore.QRect(140, 10, 133, 20))
        self.lineEdit_File.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.lineEdit_File.setFont(font)
        self.lineEdit_File.setText(_fromUtf8(""))
        self.lineEdit_File.setReadOnly(False)
        self.lineEdit_File.setObjectName(_fromUtf8("lineEdit_File"))
        self.label_Filename = QtGui.QLabel(self.dockWidgetContents)
        self.label_Filename.setGeometry(QtCore.QRect(70, 10, 60, 16))
        self.label_Filename.setObjectName(_fromUtf8("label_Filename"))
        self.checkBox_AutoUpdate = QtGui.QCheckBox(self.dockWidgetContents)
        self.checkBox_AutoUpdate.setEnabled(False)
        self.checkBox_AutoUpdate.setGeometry(QtCore.QRect(770, 130, 101, 20))
        self.checkBox_AutoUpdate.setObjectName(
            _fromUtf8("checkBox_AutoUpdate"))
        DockWidget_Analysis.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget_Analysis)
        QtCore.QMetaObject.connectSlotsByName(DockWidget_Analysis)

    def retranslateUi(self, DockWidget_Analysis):
        DockWidget_Analysis.setWindowTitle(
            _translate("DockWidget_Analysis", "Analysis", None))
        self.groupBox_Signal.setTitle(
            _translate("DockWidget_Analysis", "Signal", None))
        self.label_ExcitTruncate.setText(
            _translate("DockWidget_Analysis", "Start Signal", None))
        self.label_EndTruncate.setText(
            _translate("DockWidget_Analysis", "Stop Signal", None))
        self.label_Step.setText(
            _translate("DockWidget_Analysis", "Step (µs)", None))
        self.label_Points.setText(
            _translate("DockWidget_Analysis", "Max Points", None))
        self.checkBox_Hann.setText(
            _translate("DockWidget_Analysis", "Hann", None))
        self.checkBox_ZeroFill.setText(
            _translate("DockWidget_Analysis", "Zero (1*N)", None))
        self.checkBox_HalfHann.setText(
            _translate("DockWidget_Analysis", "1/2 Hann", None))
        self.checkBox_ZeroFillTwice.setText(
            _translate("DockWidget_Analysis", "Zero (2*N)", None))
        self.checkBox_NoZero.setText(
            _translate("DockWidget_Analysis", "No Zero", None))
        self.groupBox_Mass.setTitle(
            _translate("DockWidget_Analysis", "Mass Calibration", None))
        self.label_RefMass.setText(
            _translate("DockWidget_Analysis", "Ref. mass (u)", None))
        self.label_CycloFreq.setText(
            _translate("DockWidget_Analysis", "Cycl. Freq. (kHz)", None))
        self.label_MagFreq.setText(
            _translate("DockWidget_Analysis", "Mag. Freq (kHz)", None))
        self.label_PlotStartMass.setText(
            _translate("DockWidget_Analysis", "Plot mass limits", None))
        self.checkBox_Hold.setText(
            _translate("DockWidget_Analysis", "Hold", None))
        self.groupBox_Peak.setTitle(
            _translate("DockWidget_Analysis", "Peak Detection", None))
        self.label_PeakHeight.setText(
            _translate("DockWidget_Analysis", "Peak Height", None))
        self.label_PeakDistance.setText(
            _translate("DockWidget_Analysis", "Peak Distance", None))
        self.label_StartMass.setText(
            _translate("DockWidget_Analysis", "Start Mass", None))
        self.label_EndMass.setText(
            _translate("DockWidget_Analysis", "End Mass", None))
        self.pushButton_UpdatePlots.setText(
            _translate("DockWidget_Analysis", "Update Plots", None))
        self.label_Filename.setText(
            _translate("DockWidget_Analysis", "FILENAME", None))
        self.checkBox_AutoUpdate.setText(
            _translate("DockWidget_Analysis", "Auto Update", None))
