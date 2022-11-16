from rest_framework import serializers
from .models import Components, Users


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Components
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
