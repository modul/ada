#
# ada.py - Python frontend for ADA (Analog data aquisition)
#
# author:  Remo Gienmann <mo@liberejo.de>
# created: 2011/03/19
#

import serial, time

class Ada(object):

    def __init__(self, *args, **kwargs):
        self.com = serial.Serial(*args, **kwargs)
        if not self.com.getTimeout():
            self.com.setTimeout(1)

    def __del__(self):
        del self.com

    def __write(self, c):
        self.com.write(c)

    def __readword(self):
        w = self.com.read(2)
        if len(w) < 2:
            msb, lsb = w[0], w[1]
            return (msb << 8) + lsb
        else:
            return None

    def get_channel(self, channel):
        self.__write(str(channel))
        self.__readword()

    def get1(self):
        self.get_channel(1)

    def get2(self):
        self.get_channel(2)

    def get3(self):
        self.get_channel(3)

    def log(self, interval):
        print self.get1(), self.get2(), self.get3()
        time.sleep(interval)

