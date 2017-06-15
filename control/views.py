from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Strip
from .serializers import StripSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
import django_filters.rest_framework

from rest_framework.settings import api_settings


"""serializer_class = StripSerializer
def get_queryset(self):
	queryset = Strip.objects.all()
	filters = self.request.query_params.get('username', None)
	if username is not None:
		queryset = queryset.filter(purchaser__username=username)
	return queryset"""


def home(request):
	return render(request, 'control/home.html',{})


class StripViewSet(viewsets.ModelViewSet):
	""" API endpoint that allows users to be viewed or edited."""
	queryset = Strip.objects.all()
	serializer_class = StripSerializer

	filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
	filter_fields = ('name','num')
		
	def create(self, request, *args, **kwargs):
		serializer = StripSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		if Strip.objects.count()>=4:
			Strip.objects.first().delete()
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def perform_create(self, serializer):
		serializer.save()

	def get_success_headers(self, data):
		try:
			return {'Location': data[api_settings.URL_FIELD_NAME]}
		except (TypeError, KeyError):
			return {}

	
	
class StripList(APIView):
	""" List all Strip, or create new Strip" """
	def get(self,request,format=None):
		strips = Strip.objects.all()
		serializer = StripSerializer(strips,many=True)
		return Response(serializer.data)
	def post(self,request,form=None):
		serializer=StripSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			print("test")
			if Strip.objects.count()>=4:
				Strip.objects.first().delete()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
			
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StripDetail(APIView):
	"""Retrieve, update, or delete a Strip instance"""
	def get_object(self, pk):
		try:
			return Strip.objects.get(pk=pk)
		except Strip.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		strip = self.get_object(pk)
		serializer = StripSerializer(strip)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		strip = self.get_object(pk)
		serializer = StripSerializer(strip, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		strip = self.get_object(pk)
		strip.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		