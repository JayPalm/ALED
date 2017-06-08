from django.db import models
from django.contrib.postgres.fields import ArrayField,JSONField
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class Strip (models.Model):
	name = models.CharField(max_length=200)
	num = models.IntegerField(default=0)
	LED_COUNT = models.IntegerField(default=16)
	LED_PIN = models.IntegerField(default=18)
	LED_BRIGHTNESS = models.IntegerField(default=50)
	LED_STRIP = models.CharField(max_length=200,default="ws.WS2811_STRIP_GRB")
	color_data = JSONField(null=True,blank=True)

	'''board = ArrayField(
					ArrayField(
						models.CharField(max_length=10, blank=True, default="000000"),
						size=8,),size=8,blank=True,null=True)'''