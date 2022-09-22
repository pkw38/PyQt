import sys
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import RPi.GPIO as GPIO
import requests as req
import simplejson
from time import sleep

led = [17, 27, 22, 10]
url = "http://10.150.149.157/open"

def set_GPIO():
	GPIO.setmode(GPIO.BCM)
	for item in led:
		GPIO.setup(item, GPIO.OUT)

def server(lckNum, password):
	datas = {
		'id' : lckNum,
		'pass' : password
	}
	headers = {'Content-type': 'application/json', 'Accept': 'text/json'}
	res = req.post(url, json=datas, headers=headers)
	
	print(res.json())
	a = res.json()
	if a['SUCCESS']==True:
		print("opened")
		GPIO.output(led[lckNum - 1], GPIO.HIGH)
		sleep(1)
		GPIO.output(led[lckNum - 1], GPIO.LOW)

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QFormLayout()
        
        self.name = QLineEdit(self)
        self.password = QLineEdit(self)
        
        check_button = QPushButton("check")
        check_button.clicked.connect(self.check_button)
        
        main_layout.addRow("Name: ", self.name)
        main_layout.addRow("password: ", self.password)
        main_layout.addRow(check_button)
        
        self.setLayout(main_layout)
        self.resize(400, 200)
        self.show()
        
    def check_button(self):
        name = int(self.name.text())
        password = self.password.text()
        self.name.setText("")
        self.password.setText("")
        print(name, password)
        set_GPIO()
        server(name, password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main = Main()
    sys.exit(app.exec_())
