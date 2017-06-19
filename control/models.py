from django.db import models
from django.contrib.postgres.fields import ArrayField,JSONField
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Strip (models.Model): #rename "strip" to "Frame"
	name = models.CharField(max_length=200)
	num = models.IntegerField(default=0)
	LED_COUNT = models.IntegerField(default=16)
	LED_PIN = models.IntegerField(default=18)
	LED_BRIGHTNESS = models.IntegerField(default=50)
	LED_STRIP = models.CharField(max_length=200,default="ws.WS2811_STRIP_GRB")
	color_data = JSONField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)



#New Models
##Change
##Animation - Frames belong to animation via Foreign Key

#Consider only transmitting changes from UI

class Change(models.Model):
	"""docstring for Change"""
	led = models.IntegerField()
	new_color = models.CharField(max_length=6)
	#Create Delete method, or add delete to cusotm save

	
class Animation(models.Model):
	"""docstring for Animation"""
	name = models.CharField(max_length=200)
	max_length = models.IntegerField()

	#Set length method

	