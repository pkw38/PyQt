import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./test.ui")[0]

class MyApp(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myApp = MyApp()
	myApp.show()
	app.exec_()
