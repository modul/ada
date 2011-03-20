from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qwt5 import *

from tinyPIDmonitorui import *
import time
import numpy
from tinyPID import *
	

class tinyPIDmonitor (QMainWindow, Ui_ada):
	
	def __init__(self, parent=None):
		super(tinyPIDmonitor, self).__init__(parent)
		self.setupUi(self)
		
		self.t0 = time.time()
		self.t = []
		self.y = []
		self.w = []
		self.x = []
		
		self.view  = 0
		self.axmin = 0
		self.axmax = self.view
		self.step  = 0
		
		self.pid = None
		self.settings = QSettings("moware", "tinyPIDmonitor")
		self.restoreGeometry(self.settings.value("ui/Geometry").toByteArray())
		self.portLineEdit.setText(self.settings.value("com/Port", "/dev/ttyUSB0").toString())
		self.speedLineEdit.setText(self.settings.value("com/Baud", 19200).toString())
		self.intervalSpinBox.setValue(self.settings.value("com/Update", 1).toInt()[0])
		self.yminSpinBox.setValue(self.settings.value("plot/ymin", 0).toInt()[0])
		self.ymaxSpinBox.setValue(self.settings.value("plot/ymax", 300).toInt()[0])
		self.viewsizeSpinBox.setValue(self.settings.value("plot/View", 20).toInt()[0])
		self.scrollSpinBox.setValue(self.settings.value("plot/Scroll", 0).toInt()[0])
		self.tabWidget.setCurrentIndex(self.settings.value("ui/Tab", 0).toInt()[0])
		self.pvLabel.setText(self.settings.value("pid/PV", 0).toString())
		self.setpointSpinBox.setValue(self.settings.value("pid/SP", 0).toInt()[0])
		self.lastsetpoint = self.setpointSpinBox.value()
		self.outputSpinBox.setValue(self.settings.value("pid/Output", 0).toInt()[0])
		self.lastoutput = self.outputSpinBox.value()

		self.view  = self.viewsizeSpinBox.value()
		self.setScroll(self.scrollSpinBox.value())
		
		self.legend = QwtLegend(self.qwtPlot)
		self.legend.setGeometry(QRect(10, 10, 501, 401))
		
		gpen = QPen()
		gpen.setBrush(QColor(150,150,150))
		
		wpen = QPen()
		wpen.setBrush(QColor(0,180,0))
		wpen.setWidth(2)
		
		xpen = QPen()
		xpen.setBrush(QColor(180,0,0))
		xpen.setWidth(2)
		
		ypen = QPen()
		ypen.setBrush(QColor(0,0,180))
		ypen.setWidth(2)
		
		
		self.grid = QwtPlotGrid()
		self.grid.setMajPen(gpen)
		self.grid.attach(self.qwtPlot)
		self.gridEnable(False)
		
		self.curve_w = QwtPlotCurve("Setpoint")
		self.curve_w.attach(self.qwtPlot)
		self.curve_w.setPen(wpen)
		self.curve_w.updateLegend(self.legend)
		
		self.curve_y = QwtPlotCurve("Output")
		self.curve_y.attach(self.qwtPlot)
		self.curve_y.setPen(ypen)
		self.curve_y.updateLegend(self.legend)
		
		self.curve_x = QwtPlotCurve("Process Value")
		self.curve_x.attach(self.qwtPlot)
		self.curve_x.setPen(xpen)
		self.curve_x.updateLegend(self.legend)
		
		self.qwtPlot.setAxisScale(QwtPlot.yLeft, 0, 255)
		self.qwtPlot.setAxisTitle(QwtPlot.yLeft, "")
		self.qwtPlot.setAxisTitle(QwtPlot.xBottom, "t/s")
		self.qwtPlot.replot()
		
		self.updatetimer = QTimer()
		self.updatetimer.setInterval(self.settings.value("com/Update", 150).toInt()[0])
		self.sendtimer = QTimer()
		self.sendtimer.setInterval(1000)
		
		self.connect(self.updatetimer, SIGNAL("timeout()"), self.updateData)
		self.connect(self.sendtimer, SIGNAL("timeout()"), self.sendData)
		self.connect(self.connectButton, SIGNAL("clicked()"), self.connectPID)
		self.connect(self, SIGNAL("connected(bool)"), self.startTimers)
		self.connect(self, SIGNAL("connected(bool)"), self.connectPidSignals)
		self.connect(self.intervalSpinBox, SIGNAL("valueChanged(int)"), self.updatetimer.setInterval)
		
		if self.settings.value("com/Auto", False).toBool():
			self.connectCheckBox.toggle()
			self.connectPID()
		
		if self.settings.value("plot/Grid", False).toBool():
			self.gridCheckBox.toggle()
		
		if self.settings.value("plot/Autoscale", False).toBool():
			self.autoscaleCheckBox.toggle()
	
	
	def startTimers(self, start):
		if start:
			print "start timers"
			self.updatetimer.start()
			self.sendtimer.start()
		else:
			print "stop timers"
			self.updatetimer.stop()
			self.sendtimer.stop()
	
		
	def gridEnable(self, enable):
		self.grid.enableX(enable)
		self.grid.enableY(enable)
		self.qwtPlot.replot()
	
	
	def setView(self, length):
		if length > self.view:
			self.axmax = self.axmin + length
			self.view = length
		elif length < self.view:
			self.axmin = self.t[-2]
			self.axmax = length + self.axmin
			self.view = length
		else:
			return
		
		if self.step > 0:
			self.qwtPlot.setAxisScale(QwtPlot.xBottom, self.axmin, self.axmax)


	def setScroll(self, percent):
		self.step = percent/100.
		if self.step == 0:
			self.qwtPlot.setAxisAutoScale(QwtPlot.xBottom)


	def setYmin(self, ymin):
		ymax = self.ymaxSpinBox.value()
		self.qwtPlot.setAxisScale(QwtPlot.yLeft, ymin, ymax)


	def setYmax(self, ymax):
		ymin = self.yminSpinBox.value()
		self.qwtPlot.setAxisScale(QwtPlot.yLeft, ymin, ymax)
	
	
	def setAutoscale(self, enable):
		if enable:
			self.qwtPlot.setAxisAutoScale(QwtPlot.yLeft)
		else:
			ymin, ymax = self.yminSpinBox.value(), self.ymaxSpinBox.value()
			self.qwtPlot.setAxisScale(QwtPlot.yLeft, ymin, ymax)
		self.qwtPlot.replot()
			
		
	def updateData(self):
		""" Get data from the controller and update plot and gui. """
		
		# gather data
		self.t.append(time.time()-self.t0)
		
		try:
			x, y, w = self.pid.x, self.pid.y, self.pid.w
		except:
			self.disconnectPID()
			x = y = w = 0
			
		self.x.append(x)
		self.y.append(y)
		self.w.append(w)
		
		# update GUI
		self.errorLabel.setText(str(self.w[-1]-self.x[-1]))
		self.pvLabel.setText(str(self.x[-1]))
		if self.autoRadioButton.isChecked():
			self.outputSpinBox.setValue(self.y[-1])
		else:
			self.setpointSpinBox.setValue(self.w[-1])
		
		# update curves
		self.curve_w.setData(self.t, self.w)
		self.curve_y.setData(self.t, self.y)
		self.curve_x.setData(self.t, self.x)
		
		# cleanup points
		for i in range(len(self.t)):
			if self.t[i] < self.axmin:
				del self.t[i]
				del self.x[i]
				del self.w[i]
				del self.y[i]
			else:
				break
		
		# scroll view
		if self.t[-1] > self.axmax and self.step > 0:
			self.axmin = self.axmin + self.view*self.step
			self.axmax = self.axmax + self.view*self.step
			self.qwtPlot.setAxisScale(QwtPlot.xBottom, self.axmin, self.axmax)
			
		print "Points:", len(self.t)+len(self.w,)+len(self.x)+len(self.y),
		
		# replot
		self.qwtPlot.replot()
	
	
	def sendData(self):
		""" Send new settings to controller in case sth. has changed. """
		print "sending"
		if self.pid is None:
			return
		
		if self.manRadioButton.isChecked():
			if self.outputSpinBox.value() != self.lastoutput:
				self.pid.y = self.outputSpinBox.value()
				self.lastoutput = self.pid.y
		elif self.autoRadioButton.isChecked():
			if self.setpointSpinBox.value() != self.lastsetpoint:
				self.pid.w = self.setpointSpinBox.value()
				self.lastsetpoint = self.pid.w
	
	def connectPidSignals(self):
		"""
		Qt signals to connect only when there's communication with the controller.
		"""
		
		self.connect(self.autoRadioButton, SIGNAL("toggled(bool)"), lambda x: x and self.pid.auto())
		self.connect(self.manRadioButton, SIGNAL("toggled(bool)"), lambda x: x and self.pid.manual())
	
	
	def connectPID(self):
		"""	Setup communication with the controller. """
		
		try:
			if self.sender() == self.connectButton:
				port = self.portLineEdit.text()
				baud = self.speedLineEdit.text().toInt()[0]
			else:
				port = self.settings.value("com/Port", "/dev/ttyUSB0").toString()
				baud = self.settings.value("com/Baud", 19200).toInt()[0]
			
			self.pid = tinyPID(port=str(port), baudrate=baud)
			
		except:
			self.disconnectPID()
		else:
			self.emit(SIGNAL("connected(bool)"), True)
			self.connectLabel.setText("connected.")
			self.pid.com.readlines()
			m = self.pid.opmode
			if m == 'a':
				self.autoRadioButton.toggle()
			else:
				self.manRadioButton.toggle()
	
	
	def disconnectPID(self):
		print "disconnecting"
		self.pid = None
		self.emit(SIGNAL("connected(bool)"), False)
		self.connectLabel.setText("not connected.")
	
	
	def closeEvent(self, event):
		""" Before closing the main window, save settings. """
		
		self.settings.setValue("com/Port", self.portLineEdit.text())
		self.settings.setValue("com/Baud", self.speedLineEdit.text().toInt()[0])
		self.settings.setValue("com/Auto", self.connectCheckBox.isChecked())
		self.settings.setValue("com/Update", self.intervalSpinBox.value())
		self.settings.setValue("ui/Geometry", self.saveGeometry())
		self.settings.setValue("ui/Tab", self.tabWidget.currentIndex())
		self.settings.setValue("plot/Grid", self.gridCheckBox.isChecked())
		self.settings.setValue("plot/Autoscale", self.autoscaleCheckBox.isChecked())
		self.settings.setValue("plot/ymin", self.yminSpinBox.value())
		self.settings.setValue("plot/ymax", self.ymaxSpinBox.value())
		self.settings.setValue("plot/View", self.viewsizeSpinBox.value())
		self.settings.setValue("plot/Scroll", self.scrollSpinBox.value())
		self.settings.setValue("pid/SP", self.setpointSpinBox.value())
		self.settings.setValue("pid/PV", self.pvLabel.text().toInt()[0])
		self.settings.setValue("pid/Output", self.outputSpinBox.value())
			
	
		


if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	d = tinyPIDmonitor()
	d.show()
	app.exec_()
