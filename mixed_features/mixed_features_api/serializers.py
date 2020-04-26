from rest_framework import serializers  
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = '__all__'

class UserSerializerWithToken(serializers.ModelSerializer): 
    token = serializers.SerializerMethodField() 
    password = serializers.CharField(write_only = True)