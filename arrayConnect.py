import json,requests,time

from neopixel import *

r = requests.get('http://10.0.1.57:8000/strips/')


chose = r.json()[-1]

#Static Strip Parameters
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#Custom Strip Parameters
LED_COUNT = chose['LED_COUNT']
LED_PIN = chose['LED_PIN']
LED_BRIGHTNESS = chose['LED_BRIGHTNESS']
LED_STRIP = ws.WS2811_STRIP_GRB				#chose['LED_STRIP']

# Create NeoPixel object with appropriate configuration.
#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
#strip.begin()

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	loop=0

	while True:
		loop+=1
		if loop==1600: loop=0

		r = requests.get('http://10.0.1.56:8000/strips/')
		color=r.json()[-1]['color_data']

		for p in range(len(color)):
			strip.setPixelColor(p,int(color[p],16))
		strip.show()
		print(loop)


