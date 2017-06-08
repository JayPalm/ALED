from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from trips.models import Trip, Signup, Car,Profile
from django.contrib.auth.models import User
from .forms import SignupForm
from rest_framework import viewsets
from trips.serializers import TripSerializer, SignupSerializer, CarSerializer, UserSerializer, ProfileSerializer



from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def trip_list(request):
	trips = Trip.objects.order_by('num')
	return render(request, 'trips/trip_list.html', {'trips':trips})

def trip_detail(request, pk):
	trips = get_object_or_404(Trip, pk=pk)
	return render(request, 'trips/trip_detail.html', {'trips':trips})

def signup(request, pk):
	trips = get_object_or_404(Trip, pk=pk)
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.trip=Trip.objects.get(pk=pk)
			post.submitter = request.user
			post.subtime = timezone.now()
			post.save()
			return HttpResponseRedirect('confirm/')
	else:
		form=SignupForm()
	return render(request, 'trips/signup.html',{'form':form,'trips': trips})

def confirm(request,pk):
	trips = get_object_or_404(Trip, pk=pk)
	return render(request, 'trips/confirm.html', {'trips':trips})

def panel(request):
	trips = Trip.objects.order_by('num')
	signups = Signup.objects.all()
	sizes=[len(signups.filter(trip=i)) for i in trips]
	return render(request, 'trips/panel.html',
		{"trips":trips,"signups":signups, "sizes":sizes})

def overview(request,pk):
	trip = get_object_or_404(Trip, pk=pk)
	signups = Signup.objects.filter(trip=trip)
	cars = Car.objects.filter(trip=trip)
	return render(request,'trips/overview.html',{"trip":trip,"signups":signups,"cars":cars})




class TripViewSet(viewsets.ModelViewSet):
	""" API endpoint that allows users to be viewed or edited."""

	queryset = Trip.objects.all()
	serializer_class = TripSerializer

class CarViewSet(viewsets.ModelViewSet):
	"""API endpoint that allows groups to be viewed or edited."""
	queryset = Car.objects.all()
	serializer_class = CarSerializer

class SignupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Signup.objects.all()
	serializer_class = SignupSerializer

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer



class TripList(APIView):
	""" List all Trip, or create new Trip" """
	def get(self,request,format=None):
		trips = Trip.objects.all()
		serializer = TripSerializer(trips,many=True)
		return Response(serializer.data)

	def post(self,request,form=None):
		serializer=TripSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TripDetail(APIView):
	"""Retrieve, update, or delete a Trip instance"""
	def get_object(self, pk):
		try:
			return Trip.objects.get(pk=pk)
		except Trip.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		trip = self.get_object(pk)
		serializer = TripSerializer(trip)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		trip = self.get_object(pk)
		serializer = TripSerializer(trip, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		trip = self.get_object(pk)
		trip.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




class ProfileDetail(APIView):
	"""Retrieve, update, or delete a Profile instance"""
	def get_object(self, pk):
		try:
			return Profile.objects.get(pk=pk)
		except Profile.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		trip = self.get_object(pk)
		serializer = ProfileSerializer(trip)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		trip = self.get_object(pk)
		serializer = ProfileSerializer(trip, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		trip = self.get_object(pk)
		trip.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




class ProfileList(APIView):
	""" List all Profile, or create new Profile" """
	def get(self,request,format=None):
		trips = Profile.objects.all()
		serializer = ProfileSerializer(profile,many=True)
		return Response(serializer.data)

	def post(self,request,form=None):
		serializer=ProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

