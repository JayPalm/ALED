"""

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	loop=0

	while True:
		t1 = time.clock()
		loop+=1
		if loop==1600: loop=0
		t2 = time.clock()
		r = requests.get('http://10.0.1.57:8000/strips/')

		t3 = time.clock()
		colorA=r.json()
		t3A = time.clock()
		colorB=colorA[-1]
		t3B = time.clock()
		colorC = colorB['color_data']
		t4 = time.clock()


		for p in range(len(color)):
			strip.setPixelColor(p,int(colorC[p],16))
		t5 = time.clock()
		strip.show()
		t6 = time.clock()
		print("Times:", t3-t4,t3A-t3,t3B-t3A,t3C-t3B,t4-t3C)
"""


import json,requests,time,ujson

from neopixel import *
try:
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
except:
	print("Server unreachable. Please try again")
# Create NeoPixel object with appropriate configuration.
#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
#strip.begin()

if __name__ == '__main__':
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	loop=0
	loop_times=[]


	while True:
		#t1 = time.process_time()
		if loop==1600: loop=0
		try:
			r = requests.get('http://10.0.1.57:8000/strips/')
			r.encoding='UTF-8'
			color=json.loads(r.text)[-1]['color_data']
			
			for p in range(len(color)):
				strip.setPixelColor(p,int(color[p],16))
			strip.show()

		except:
			print("Server unreachable")
		
		
		print("loop",loop)
		loop+=1



def comp():
	ob = Strip.objects.all()
	for i in range(4): 
		print(ob[i].color_data[0:15])

	
