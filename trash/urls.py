from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^_list/$', views.trip_list, name='trip_list'),
	url(r'^(?P<pk>\d+)/$', views.trip_detail, name='trip_detail'),
	url(r'^(?P<pk>\d+)/signup/$',views.signup, name = 'signup'),
	url(r'^(?P<pk>\d+)/signup/confirm/$',views.confirm, name = 'confirm'),
	url(r'^_panel/$', views.panel, name = 'panel'),
	url(r'^_overview_(?P<pk>\d+)',views.overview, name = 'overview')

	#url(r'^overview_(?P<pk>\d+)/$',views.overview, name='overview')
]