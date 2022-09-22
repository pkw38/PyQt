import RPi.GPIO as GPIO
import requests as req
import simplejson
from time import sleep

led = [17, 27, 22, 10]

GPIO.setmode(GPIO.BCM)

for item in led:
	GPIO.setup(item, GPIO.OUT)


url = "http://10.150.149.31/open"

lckNum = int(input("Number : "))
password = input("password : ")
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
	sleep(2)
	GPIO.output(led[lckNum - 1], GPIO.LOW)
