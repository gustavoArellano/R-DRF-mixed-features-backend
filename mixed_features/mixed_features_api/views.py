from django.shortcuts import render 
from django.http import JsonResponse 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .serializers import UserSerializer 
from . import models 


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/user-list/',
        'Detail View': '/user-detail/<str:pk>/',
        'Create': '/user-create/',
        'Update': '/user-update/<str:pk>/',
        'Delete': '/user-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['POST']) 
def signUp(request):
    serializer = UserSerializer(data = request.data) 
    if serializer.is_valid():
        serializer.save()

@api_view(['GET'])
def userList(request): 
    users = models.User.objects.all()
    serializer = UserSerializer(users, many = True) 
    return Response(serializer.data)

