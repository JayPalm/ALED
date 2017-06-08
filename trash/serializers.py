from django.contrib.auth.models import User, Group
from rest_framework import serializers
from trips.models import Trip, Car, Signup,Profile


class TripSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Trip
		fields = ('num', 'title','description','weekend', 'available', 'car_quant', 'signup_quant')


class CarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Car
		fields = ('trip','owner','capacityWG','awd','chains','available_seats','leave_berkeley_day', 'leave_berkeley_time')


class SignupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Signup
		fields = ('trip', 'date', 'submitter', 'fname', 'lname', 'phone','email','has_car','car' ,'car_auto_added' ,'leave_berkeley_day','leave_berkeley_time')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
		

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('pic', 'email', 'iceCream')
		


