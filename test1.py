import sys
from PyQt5.QtWidgets import *
import RPi.GPIO as GPIO
import requests as req
import simplejson
from time import sleep

led = [17, 27, 22, 10]

GPIO.setmode(GPIO.BCM)

for item in led:
	GPIO.setup(item, GPIO.OUT)

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QFormLayout()
        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        line_lckNum = QLineEdit()
        line_pass = QLineEdit()
        
        main_layout.addRow("Number: ", line_lckNum)
        main_layout.addRow("password: ", line_pass)
        
        main_layout.Row(layout)

        pushbutton = QPushButton("led on")
        pushbutton.clicked.connect(self.led_on)
        main_layout.addWidget(pushbutton)
        
        pushbutton = QPushButton("led off")
        pushbutton.clicked.connect(self.led_off)
        main_layout.addWidget(pushbutton)

        self.lineedit = QLineEdit()
        main_layout.addWidget(self.lineedit)

        combobox = QComboBox()
        combobox.addItems(["dog", "cat", "rabbit", "lion"])
        combobox.currentTextChanged.connect(self.combobox_changed)
        main_layout.addWidget(combobox)

        self.lineedit_combox = QLineEdit()
        main_layout.addWidget(self.lineedit_combox)

        checkbox = QCheckBox("item")
        checkbox.stateChanged.connect(self.checkbox_changed)
        main_layout.addWidget(checkbox)

        self.linedit_checkbox = QLineEdit()
        main_layout.addWidget(self.linedit_checkbox)

        radio_1, radio_2 = QRadioButton("A"), QRadioButton("B")
        radio_1.toggled.connect(self.radio_1_toggled)
        radio_2.toggled.connect(self.radio_2_toggled)
        main_layout.addWidget(radio_1)
        main_layout.addWidget(radio_2)
        self.lineedit_radio_1 = QLineEdit()
        self.lineedit_radio_2 = QLineEdit()
        main_layout.addWidget(self.lineedit_radio_1)
        main_layout.addWidget(self.lineedit_radio_2)

        self.setLayout(main_layout)
        self.resize(400, 400)
        self.show()

    ###############
    ### actions ###
    ###############
    def led_on(self):
        self.lineedit.setText("button clicked.")
        print(lckNum, password)
        GPIO.output(led[0], GPIO.HIGH)
        
    def led_off(self):
        self.lineedit.setText("button clicked.")
        print('hello')
        GPIO.output(led[0], GPIO.LOW)

    def combobox_changed(self, item):
        self.lineedit_combox.setText('Your selection : ' + item)

    def checkbox_changed(self, state):
        self.linedit_checkbox.setText(str(state))

    def radio_1_toggled(self, state):
        self.lineedit_radio_1.setText(str(state))

    def radio_2_toggled(self, state):
        self.lineedit_radio_2.setText(str(state))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
