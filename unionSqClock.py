from PySide import QtCore, QtGui

class DigitalClock(QtGui.QWidget):
	def __init__(self):
		super(DigitalClock, self).__init__()
		self.initUI()
		timer = QtCore.QTimer(self)
		timer.timeout.connect(self.showlcd)
		timer.start(1)
		self.showlcd()

	def initUI(self):

		self.lcd = QtGui.QLCDNumber(self)
		self.lcd.setDigitCount(21)          # change the number of digits displayed
		self.setGeometry(30, 30, 800, 600)
		self.setWindowTitle('Union Square Clock')

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(self.lcd)
		self.setLayout(vbox)

		self.show()

	def showlcd(self):
		time = QtCore.QTime.currentTime()
		text = time.toString('hh:mm:ss:zzz')

		# add reverse
		hours = str(24-int(text[:2]))
		mins = str(59-int(text[3:5]))
		secs = str(59-int(text[6:8]))
		text += ':' + secs + ':' + mins + ':' + hours
		self.lcd.display(text)

if __name__ == '__main__':
	import time, sys
	app = QtGui.QApplication(sys.argv)
	clock = DigitalClock()
	clock.show()
	sys.exit(app.exec_())