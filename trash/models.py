from django.db import models
#from django.contrib.postgres.fields import ArrayField
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from utilities.utilities import *


class Trip(models.Model):
	num = models.IntegerField(default=0)
	title = models.CharField(max_length=200)
	#image = models.ImageField()
	description = models.TextField()
	weekend = models.CharField(max_length=200)
	available = models.BooleanField(default=False)
	car_quant = models.IntegerField(default=0)
	signup_quant = models.IntegerField(default=0)
	#size = models.IntegerField(default=0)

	def __str__(self):
		return str(self.pk)
	def open(self):
		self.available = True
		self.save()
	def signup_list(self):
		return Signup.objects.filter(trip__id=self.pk)
	def cars(self):
		return Car.objects.filter(trip__pk=self.pk)
	def save(self):
		self.car_quant=self.cars().count()
		self.signup_quant = self.signup_list().count()
		super(Trip, self).save()

yesno = ((0,"No"),(1,"Yes"))

class Car(models.Model):
	trip = models.ForeignKey('Trip')
	owner = models.OneToOneField('Signup',related_name='+')
	capacityWG=models.IntegerField(default=5)
	awd = models.BooleanField(choices = yesno, default=0)
	chains = models.BooleanField(choices=yesno, default=0)
	available_seats = models.IntegerField()
	leave_berkeley_day = models.BooleanField()
	leave_berkeley_time = models.FloatField()
	#passengers = models.ForeignKey()

	def __str__(self):
		return str(self.pk)
	def passengers(self):
		return Signup.objects.filter(car__id=self.pk)
	def save(self):
		self.available_seats=self.capacityWG-self.passengers().count()
		self.leave_berkeley_day = self.owner.leave_berkeley_day
		self.leave_berkeley_time = self.owner.leave_berkeley_time
		super(Car, self).save()
	#c1=Car(index=1,owner="George",capacityWG=5,awd=1,chains=0)
frisat = ((0,"Friday"),(1,"Saturday"))

class Signup(models.Model):
	trip = models.ForeignKey('Trip')
	date = models.DateTimeField(default=timezone.now)
	submitter = models.ForeignKey('auth.User')
	fname = models.CharField("First Name", max_length=200,)
	lname = models.CharField("Last Name", max_length=200, )
	phone = models.CharField("Phone Number", max_length=9)
	email = models.EmailField("Email Adress",max_length=200)
	has_car = models.BooleanField('Do you have a Car?', choices=yesno, default=0)
	car = models.ForeignKey('Car', on_delete=models.SET_NULL,blank=True,null=True)
	car_auto_added = models.BooleanField(default=False)
	#car_TB = models.ForeignKey('Car')
	leave_berkeley_day=models.BooleanField("When can you leave Berkeley", max_length=200,choices=frisat,default=0)
	leave_berkeley_time=models.FloatField("When can you leave Berkeley",choices=list_hours(10,20), max_length=200,default=10)
	def __str__(self):
		return self.fname


class Profile(models.Model):
	pic = models.CharField("pic", max_length=200)
	email = models.CharField("email", max_length=300)
	iceCream = models.CharField("iceCream",max_length=200)


"""class LEDArray(models.Model):
	array = ArrayField(
		ArrayField(
			models.CharField(max_length=10,blank=True),
			size=8,
			),
		size=8,
		)"""
