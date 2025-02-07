from rest_framework import serializers
from .models import Usersv2

class Usersv2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usersv2
        fields = '__all__'

class Usersv2SerializerRangeFollowers(serializers.ModelSerializer):
    class Meta:
        model = Usersv2
        fields = ['first_name', 'last_name', 'followers']

