from django.db import models
#from django.contrib.postgres.fields import ArrayField
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
#from utilities.utilities import *


class Strip (models.Model):
	name = models.CharField(max_length=200)
	num = models.IntegerField(default=0)
	LED_COUNT = models.IntegerField(default=16)
	LED_PIN = models.IntegerField(default=18)      # GPIO pin connected to the pixels (18 uses PWM!).
	LED_BRIGHTNESS = models.IntegerField(default=50)    # Set to 0 for darkest and 255 for brightest
	LED_STRIP = models.CharField(max_length=200,default="ws.WS2811_STRIP_GRB")
