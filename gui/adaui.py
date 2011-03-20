# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ada.ui'
#
# Created: Sun Mar 20 23:52:16 2011
#      by: PySide uic UI code generator
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qwt5 import *

class Ui_ada(object):
    def setupUi(self, ada):
        ada.setObjectName("ada")
        ada.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ada.sizePolicy().hasHeightForWidth())
        ada.setSizePolicy(sizePolicy)
        ada.setMinimumSize(QtCore.QSize(800, 600))
        ada.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(ada)
        self.centralwidget.setObjectName("centralwidget")
        self.qwtPlot = QwtPlot(self.centralwidget)
        self.qwtPlot.setGeometry(QtCore.QRect(10, 10, 771, 481))
        self.qwtPlot.setObjectName("qwtPlot")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 510, 781, 81))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.Mon = QtGui.QWidget()
        self.Mon.setObjectName("Mon")
        self.widget = QtGui.QWidget(self.Mon)
        self.widget.setGeometry(QtCore.QRect(160, 10, 461, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ch1label = QtGui.QLabel(self.widget)
        self.ch1label.setObjectName("ch1label")
        self.horizontalLayout_3.addWidget(self.ch1label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.ch2label = QtGui.QLabel(self.widget)
        self.ch2label.setObjectName("ch2label")
        self.horizontalLayout_3.addWidget(self.ch2label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.ch3label = QtGui.QLabel(self.widget)
        self.ch3label.setObjectName("ch3label")
        self.horizontalLayout_3.addWidget(self.ch3label)
        self.tabWidget.addTab(self.Mon, "")
        self.Plot = QtGui.QWidget()
        self.Plot.setObjectName("Plot")
        self.widget1 = QtGui.QWidget(self.Plot)
        self.widget1.setGeometry(QtCore.QRect(60, 10, 651, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridCheckBox = QtGui.QCheckBox(self.widget1)
        self.gridCheckBox.setObjectName("gridCheckBox")
        self.horizontalLayout.addWidget(self.gridCheckBox)
        self.autoscaleCheckBox = QtGui.QCheckBox(self.widget1)
        self.autoscaleCheckBox.setObjectName("autoscaleCheckBox")
        self.horizontalLayout.addWidget(self.autoscaleCheckBox)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.yminSpinBox = QtGui.QSpinBox(self.widget1)
        self.yminSpinBox.setAccelerated(True)
        self.yminSpinBox.setMaximum(9999)
        self.yminSpinBox.setObjectName("yminSpinBox")
        self.horizontalLayout.addWidget(self.yminSpinBox)
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.ymaxSpinBox = QtGui.QSpinBox(self.widget1)
        self.ymaxSpinBox.setAccelerated(True)
        self.ymaxSpinBox.setMinimum(0)
        self.ymaxSpinBox.setMaximum(9999)
        self.ymaxSpinBox.setProperty("value", QtCore.QVariant(5))
        self.ymaxSpinBox.setObjectName("ymaxSpinBox")
        self.horizontalLayout.addWidget(self.ymaxSpinBox)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.vrefDoubleSpinBox = QtGui.QDoubleSpinBox(self.widget1)
        self.vrefDoubleSpinBox.setMinimum(-99.0)
        self.vrefDoubleSpinBox.setProperty("value", QtCore.QVariant(5.0))
        self.vrefDoubleSpinBox.setObjectName("vrefDoubleSpinBox")
        self.horizontalLayout.addWidget(self.vrefDoubleSpinBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.viewsizeSpinBox = QtGui.QSpinBox(self.widget1)
        self.viewsizeSpinBox.setMinimum(1)
        self.viewsizeSpinBox.setMaximum(9999)
        self.viewsizeSpinBox.setObjectName("viewsizeSpinBox")
        self.horizontalLayout.addWidget(self.viewsizeSpinBox)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.scrollSpinBox = QtGui.QSpinBox(self.widget1)
        self.scrollSpinBox.setAccelerated(True)
        self.scrollSpinBox.setMaximum(100)
        self.scrollSpinBox.setObjectName("scrollSpinBox")
        self.horizontalLayout.addWidget(self.scrollSpinBox)
        self.tabWidget.addTab(self.Plot, "")
        self.Com = QtGui.QWidget()
        self.Com.setObjectName("Com")
        self.widget2 = QtGui.QWidget(self.Com)
        self.widget2.setGeometry(QtCore.QRect(60, 10, 651, 31))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.portLabel = QtGui.QLabel(self.widget2)
        self.portLabel.setObjectName("portLabel")
        self.horizontalLayout_2.addWidget(self.portLabel)
        self.portLineEdit = QtGui.QLineEdit(self.widget2)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout_2.addWidget(self.portLineEdit)
        self.speedLabel = QtGui.QLabel(self.widget2)
        self.speedLabel.setObjectName("speedLabel")
        self.horizontalLayout_2.addWidget(self.speedLabel)
        self.speedLineEdit = QtGui.QLineEdit(self.widget2)
        self.speedLineEdit.setObjectName("speedLineEdit")
        self.horizontalLayout_2.addWidget(self.speedLineEdit)
        self.intervalLabel = QtGui.QLabel(self.widget2)
        self.intervalLabel.setObjectName("intervalLabel")
        self.horizontalLayout_2.addWidget(self.intervalLabel)
        self.intervalSpinBox = QtGui.QSpinBox(self.widget2)
        self.intervalSpinBox.setMinimum(1)
        self.intervalSpinBox.setMaximum(9999)
        self.intervalSpinBox.setProperty("value", QtCore.QVariant(1000))
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.horizontalLayout_2.addWidget(self.intervalSpinBox)
        self.connectCheckBox = QtGui.QCheckBox(self.widget2)
        self.connectCheckBox.setObjectName("connectCheckBox")
        self.horizontalLayout_2.addWidget(self.connectCheckBox)
        self.connectButton = QtGui.QPushButton(self.widget2)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_2.addWidget(self.connectButton)
        self.connectLabel = QtGui.QLabel(self.widget2)
        self.connectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connectLabel.setObjectName("connectLabel")
        self.horizontalLayout_2.addWidget(self.connectLabel)
        self.tabWidget.addTab(self.Com, "")
        ada.setCentralWidget(self.centralwidget)

        self.retranslateUi(ada)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.gridCheckBox, QtCore.SIGNAL("toggled(bool)"), ada.gridEnable)
        QtCore.QObject.connect(self.autoscaleCheckBox, QtCore.SIGNAL("toggled(bool)"), ada.setAutoscale)
        QtCore.QObject.connect(self.yminSpinBox, QtCore.SIGNAL("valueChanged(int)"), ada.setYmin)
        QtCore.QObject.connect(self.ymaxSpinBox, QtCore.SIGNAL("valueChanged(int)"), ada.setYmax)
        QtCore.QObject.connect(self.vrefDoubleSpinBox, QtCore.SIGNAL("valueChanged(double)"), ada.setVref)
        QtCore.QObject.connect(self.viewsizeSpinBox, QtCore.SIGNAL("valueChanged(int)"), ada.setView)
        QtCore.QObject.connect(self.scrollSpinBox, QtCore.SIGNAL("valueChanged(int)"), ada.setScroll)
        QtCore.QObject.connect(self.autoscaleCheckBox, QtCore.SIGNAL("toggled(bool)"), self.yminSpinBox.setDisabled)
        QtCore.QObject.connect(self.autoscaleCheckBox, QtCore.SIGNAL("toggled(bool)"), self.ymaxSpinBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(ada)

    def retranslateUi(self, ada):
        ada.setWindowTitle(QtGui.QApplication.translate("ada", "Analog Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ada", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Channel 1:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ch1label.setText(QtGui.QApplication.translate("ada", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ada", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Channel 2:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ch2label.setText(QtGui.QApplication.translate("ada", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ada", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Channel 3:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ch3label.setText(QtGui.QApplication.translate("ada", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Mon), QtGui.QApplication.translate("ada", "Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.gridCheckBox.setText(QtGui.QApplication.translate("ada", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.autoscaleCheckBox.setText(QtGui.QApplication.translate("ada", "Autoscale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ada", "y", None, QtGui.QApplication.UnicodeUTF8))
        self.yminSpinBox.setSuffix(QtGui.QApplication.translate("ada", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ada", "–", None, QtGui.QApplication.UnicodeUTF8))
        self.ymaxSpinBox.setSuffix(QtGui.QApplication.translate("ada", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ada", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">V</span><span style=\" font-size:10pt; vertical-align:sub;\">ref</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.vrefDoubleSpinBox.setSuffix(QtGui.QApplication.translate("ada", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ada", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.viewsizeSpinBox.setSuffix(QtGui.QApplication.translate("ada", "s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ada", "Scroll", None, QtGui.QApplication.UnicodeUTF8))
        self.scrollSpinBox.setSuffix(QtGui.QApplication.translate("ada", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Plot), QtGui.QApplication.translate("ada", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.portLabel.setText(QtGui.QApplication.translate("ada", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.portLineEdit.setText(QtGui.QApplication.translate("ada", "/dev/ttyUSB0", None, QtGui.QApplication.UnicodeUTF8))
        self.speedLabel.setText(QtGui.QApplication.translate("ada", "Speed:", None, QtGui.QApplication.UnicodeUTF8))
        self.speedLineEdit.setText(QtGui.QApplication.translate("ada", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.intervalLabel.setText(QtGui.QApplication.translate("ada", "Interval:", None, QtGui.QApplication.UnicodeUTF8))
        self.intervalSpinBox.setSuffix(QtGui.QApplication.translate("ada", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.connectCheckBox.setText(QtGui.QApplication.translate("ada", "Autoconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("ada", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.connectLabel.setText(QtGui.QApplication.translate("ada", "not connected", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Com), QtGui.QApplication.translate("ada", "Com", None, QtGui.QApplication.UnicodeUTF8))

#from qwt_plot import QwtPlot
