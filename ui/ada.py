#
# ada.py - Python frontend for ADA (Analog data aquisition)
#
# author:  Remo Gienmann <mo@liberejo.de>
# created: 2011/03/19
#

import serial, time

resolution = 10

class Ada(object):
	"""
	Frontend to Ada (Analog Data Aquisiton).
	
	Methods:
	--------
	
	setVref(vref):  sets the reference voltage to calculate ADC voltage read
	get_channel(channel): get the reading of the ADC channel 'channel'.
	get1(): get the reading of channel 1
	get2(): get the reading of channel 2
	get3(): get the reading of channel 3
	get_all(): read all channels
	log(interval): read all channels continuously with a pause of 'interval' between
	"""
	
	
	def __init__(self, *args, **kwargs):
		self.com = serial.Serial(*args, **kwargs)
		if not self.com.getTimeout():
			self.com.setTimeout(1)

		self.vref = 5.0

	def __del__(self):
		del self.com

	def __write(self, c):
		self.com.write(c)

	def __readword(self):
		w = self.com.read(2)
		if len(w) == 2:
			msb, lsb = ord(w[0]), ord(w[1])
			return (msb << 8) + lsb
		else:
			return None

	def setVref(self, vref):
		self.vref = vref

	def get_channel(self, channel):
		self.__write(str(channel))
		adc  = self.__readword()
		if adc is not None and self.vref != 0 and self.vref is not None:
			volt = adc * self.vref / ((2**resolution)-1)
			return volt
		else:
			return adc

	def get1(self):
		return self.get_channel(1)

	def get2(self):
		return self.get_channel(2)

	def get3(self):
		return self.get_channel(3)

	def get_all(self):
		return (self.get1(), self.get2(), self.get3())

	def log(self, interval):
		print self.get1(), self.get2(), self.get3()
		time.sleep(interval)

