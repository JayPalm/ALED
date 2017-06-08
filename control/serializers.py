from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Strip


class StripSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Strip
		fields = ('name','num','LED_COUNT','LED_PIN','LED_BRIGHTNESS','LED_STRIP')



"""class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
		"""