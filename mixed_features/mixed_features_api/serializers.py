from rest_framework import serializers  
from .models import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id', 'image', 'first_name', 'last_name', 'username', 'email', 'zip_code', 
        # extra_kwargs = {'password': {'write_only': True}}

class UserSerializerWithToken(serializers.ModelSerializer): 
    token = serializers.SerializerMethodField() 
    password = serializers.CharField(write_only = True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data): 
        user = User(
            image = validated_data['image'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            zip_code = validated_data['zip_code'],
            password = make_password(validated_data['password'])
        )
        user.save()
        return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('proifle')
    #     profile = instance.profile

        # instance

    class Meta: 
        model = User
        fields = '__all__' 
        extra_kwargs = {'password': {'write_only': True}}