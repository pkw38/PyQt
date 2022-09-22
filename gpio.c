#include <stdio.h>
#include <wiringPi.h>

int led = 17;

int main(void) {
	wiringPiSetupGpio();
	pinMode(led, OUTPUT);
	
	digitalWrite(led, HIGH);
	
	return 0;
}
