from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qwt5 import *

from adaui import *
import time
import numpy
from ada import *
	

class Adaqt (QMainWindow, Ui_ada):
	"""
	Qt frontend to Ada (Analog Data Aquisition).
	"""
	
	def __init__(self, parent=None):
		super(Adaqt, self).__init__(parent)
		self.setupUi(self)
		
		self.t = []
		self.ch1 = []
		self.ch2 = []
		self.ch3 = []
		
		self.view  = 0
		self.axmin = 0
		self.axmax = self.view
		self.step  = 0
		
		self.ada = None
		self.settings = QSettings("moware", "adaqt")
		self.restoreGeometry(self.settings.value("ui/Geometry").toByteArray())
		self.portLineEdit.setText(self.settings.value("com/Port", "/dev/ttyUSB0").toString())
		self.speedLineEdit.setText(self.settings.value("com/Baud", 19200).toString())
		self.intervalSpinBox.setValue(self.settings.value("com/Update", 1).toInt()[0])
		self.yminSpinBox.setValue(self.settings.value("plot/ymin", 0).toInt()[0])
		self.ymaxSpinBox.setValue(self.settings.value("plot/ymax", 300).toInt()[0])
		self.viewsizeSpinBox.setValue(self.settings.value("plot/View", 20).toInt()[0])
		self.scrollSpinBox.setValue(self.settings.value("plot/Scroll", 0).toInt()[0])
		self.vrefDoubleSpinBox.setValue(self.settings.value("ada/vref", 0).toInt()[0])
		self.tabWidget.setCurrentIndex(0)

		self.view  = self.viewsizeSpinBox.value()
		self.setScroll(self.scrollSpinBox.value())
				
		gpen = QPen()
		gpen.setBrush(QColor(150,150,150))
		
		pen1 = QPen()
		pen1.setBrush(QColor(0,0xB4,0))
		pen1.setWidth(2)
		
		pen2 = QPen()
		pen2.setBrush(QColor(0xB4,0,0))
		pen2.setWidth(2)
		
		pen3 = QPen()
		pen3.setBrush(QColor(0,0,0xB4))
		pen3.setWidth(2)
		
		
		self.grid = QwtPlotGrid()
		self.grid.setMajPen(gpen)
		self.grid.attach(self.qwtPlot)
		self.gridEnable(False)
		
		self.curve_ch1 = QwtPlotCurve("Channel 1")
		self.curve_ch1.attach(self.qwtPlot)
		self.curve_ch1.setPen(pen1)
		
		self.curve_ch2 = QwtPlotCurve("Channel 2")
		self.curve_ch2.attach(self.qwtPlot)
		self.curve_ch2.setPen(pen2)
		
		self.curve_ch3 = QwtPlotCurve("Channel 3")
		self.curve_ch3.attach(self.qwtPlot)
		self.curve_ch3.setPen(pen3)

		
		self.qwtPlot.setAxisScale(QwtPlot.yLeft, 0, 5)
		self.qwtPlot.setAxisTitle(QwtPlot.yLeft, "")
		self.qwtPlot.setAxisTitle(QwtPlot.xBottom, "t/s")
		self.qwtPlot.replot()
		
		self.updatetimer = QTimer()
		self.updatetimer.setInterval(self.settings.value("com/Update", 150).toInt()[0])
				
		self.connect(self.updatetimer, SIGNAL("timeout()"), self.updateData)
		self.connect(self.connectButton, SIGNAL("clicked()"), self.connectAda)
		self.connect(self, SIGNAL("connected(bool)"), self.startTimer)
		self.connect(self.intervalSpinBox, SIGNAL("valueChanged(int)"), self.updatetimer.setInterval)
		
		if self.settings.value("com/Auto", False).toBool():
			self.connectCheckBox.toggle()
			self.connectAda()
		
		if self.settings.value("plot/Grid", False).toBool():
			self.gridCheckBox.toggle()
		
		if self.settings.value("plot/Autoscale", False).toBool():
			self.autoscaleCheckBox.toggle()
	
	
	def startTimer(self, start):
		if start:
			print "start timer"
			self.t0 = time.time()
			self.updatetimer.start()
		else:
			print "stop timer"
			self.updatetimer.stop()
	
		
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
		self.qwtPlot.replot()


	def setYmax(self, ymax):
		ymin = self.yminSpinBox.value()
		self.qwtPlot.setAxisScale(QwtPlot.yLeft, ymin, ymax)
		self.qwtPlot.replot()
	
	
	def setAutoscale(self, enable):
		if enable:
			self.qwtPlot.setAxisAutoScale(QwtPlot.yLeft)
		else:
			ymin, ymax = self.yminSpinBox.value(), self.ymaxSpinBox.value()
			self.qwtPlot.setAxisScale(QwtPlot.yLeft, ymin, ymax)
		self.qwtPlot.replot()
	
	
	def setVref(self, val=None):
		if self.ada is None:
			return 
			
		if val is None:
			vref = self.vrefDoubleSpinBox.value()
		else:
			vref = val
			
		self.ada.setVref(vref)
		
	
	def resetTime(self):
		""" Reset the time axis. """
		print "reset time axis"
		if self.scrollSpinBox.value() == 0 \
		   or len(self.t) == 0 :
			return
		else:
			self.updatetimer.stop()
			
			t0 = self.t[0]
			self.t0 =  time.time() - self.t[-1] + t0
			self.t = [t-t0 for t in self.t]
						
			self.axmax = self.view
			self.axmin = 0
			self.qwtPlot.setAxisScale(QwtPlot.xBottom, self.axmin, self.axmax)
			
			self.updatetimer.start()
	
		
	def updateData(self):
		""" Get data from the device and update plot and gui. """
		
		# gather data
		self.t.append(time.time()-self.t0)
		
		try:
			ch1 = self.ada.get1() or 0
			ch2 = self.ada.get2() or 0
			ch3 = self.ada.get3() or 0
		except:
			self.disconnectAda()
			ch1 = ch2 = ch3 = 0

		self.ch1.append(ch1)
		self.ch2.append(ch2)
		self.ch3.append(ch3)
		
		# update GUI
		if self.vrefDoubleSpinBox.value() == 0:
			self.ch1label.setText("<font color='#00B400' size='5'>%i</font>" % ch1)
			self.ch2label.setText("<font color='#B40000' size='5'>%i</font>" % ch2)
			self.ch3label.setText("<font color='#0000B4' size='5'>%i</font>" % ch3)
			self.qwtPlot.setAxisTitle(QwtPlot.yLeft, "Voltage/LSB")
		else:
			self.ch1label.setText("<font color='#00B400' size='5'>%.3fV</font>" % ch1)
			self.ch2label.setText("<font color='#B40000' size='5'>%.3fV</font>" % ch2)
			self.ch3label.setText("<font color='#0000B4' size='5'>%.3fV</font>" % ch3)
			self.qwtPlot.setAxisTitle(QwtPlot.yLeft, "Voltage/V")
		
				
		# update curves
		self.curve_ch1.setData(self.t, self.ch1)
		self.curve_ch3.setData(self.t, self.ch2)
		self.curve_ch2.setData(self.t, self.ch3)
		
		# cleanup points
		for i in range(len(self.t)):
			if self.t[i] < self.axmin:
				del self.t[i]
				del self.ch1[i]
				del self.ch2[i]
				del self.ch3[i]
			else:
				break
		
		# scroll view
		if self.t[-1] > self.axmax and self.step > 0:
			self.axmin = self.axmin + self.view*self.step
			self.axmax = self.axmax + self.view*self.step
			self.qwtPlot.setAxisScale(QwtPlot.xBottom, self.axmin, self.axmax)
			
		# replot
		self.qwtPlot.replot()


	def connectAda(self):
		"""	Setup communication with the device. """
		
		try:
			if self.sender() == self.connectButton:
				port = self.portLineEdit.text()
				baud = self.speedLineEdit.text().toInt()[0]
			else:
				port = self.settings.value("com/Port", "/dev/ttyUSB0").toString()
				baud = self.settings.value("com/Baud", 19200).toInt()[0]
			
			self.ada = Ada(port=str(port), baudrate=baud)
			
		except:
			self.disconnectAda()
		else:
			self.emit(SIGNAL("connected(bool)"), True)
			self.connectLabel.setText("connected.")
			self.ada.com.readlines()
			self.setVref()
	
	
	def disconnectAda(self):
		print "disconnecting"
		self.ada = None
		self.emit(SIGNAL("connected(bool)"), False)
		self.connectLabel.setText("not connected.")
	
	
	def closeEvent(self, event):
		""" Before closing the main window, save settings. """
		
		self.settings.setValue("com/Port", self.portLineEdit.text())
		self.settings.setValue("com/Baud", self.speedLineEdit.text().toInt()[0])
		self.settings.setValue("com/Auto", self.connectCheckBox.isChecked())
		self.settings.setValue("com/Update", self.intervalSpinBox.value())
		self.settings.setValue("ui/Geometry", self.saveGeometry())
		self.settings.setValue("plot/Grid", self.gridCheckBox.isChecked())
		self.settings.setValue("plot/Autoscale", self.autoscaleCheckBox.isChecked())
		self.settings.setValue("plot/ymin", self.yminSpinBox.value())
		self.settings.setValue("plot/ymax", self.ymaxSpinBox.value())
		self.settings.setValue("plot/View", self.viewsizeSpinBox.value())
		self.settings.setValue("plot/Scroll", self.scrollSpinBox.value())
		self.settings.setValue("ada/vref", self.vrefDoubleSpinBox.value())
		


if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	d = Adaqt()
	d.show()
	app.exec_()
