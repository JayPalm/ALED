"""import json,requests,time

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
	loop_times=[]


	while True:
		t1 = time.process_time()
		
		if loop==1600: loop=0
		t2 = time.process_time()
		r = requests.get('http://10.0.1.57:8000/strips/')

		t3 = time.process_time()
		r.encoding='UTF-8'
		colorA=json.loads(r.text)
		t3A = time.process_time()

		colorB=colorA[-1]
		t3B = time.process_time()

		colorC = colorB['color_data']
		t4 = time.process_time()


		for p in range(len(colorC)):
			strip.setPixelColor(p,int(colorC[p],16))
		t5 = time.process_time()
		strip.show()
		t6 = time.process_time()
		#print("Times:", t6-t1)
		#t3-t4,t3A-t3,t3B-t3A,t4-t3B
		loop_times.append((t3A-t3))
		print(loop_times[loop],loop)
		loop+=1

i=0
while True:
	t1 = time.process_time()
	r = requests.get('http://10.0.1.57:8000/strips/')
	t2 = time.process_time()
	r.encoding='UTF-8'
	colorA=ujson.loads(r.text)
	t3A = time.process_time()

	colorB=colorA[-1]
	t3B = time.process_time()

	colorC = colorB['color_data']
	t4 = time.process_time()


	for p in range(len(colorC)): print(colorC[p])
		
	t5 = time.process_time()
	
	t6 = time.process_time()
	
	loop_times.append((t1,t6))
	print(t1)
	i+=1

