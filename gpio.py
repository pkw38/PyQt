from gpiozero import LED
from time import sleep

red_led = LED(17)

while True:
	red_led.on()
