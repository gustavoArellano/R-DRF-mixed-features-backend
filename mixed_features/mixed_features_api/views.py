from django.shortcuts import render 
from django.http import JsonResponse 
from rest_framework import permissions, status
from rest_framework.decorators import api_view 
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import UserSerializer, UserSerializerWithToken
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

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format = None):
        serializer = UserSerializerWithToken(data = request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, print("User created succesfully!"))
        return Response(serializer.errors, print("Something went wrong with create!!!"))

@api_view(['GET'])
def userList(request): 
    users = models.User.objects.all()
    serializer = UserSerializer(users, many = True) 
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    user = models.User.objects.get(id = pk)
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
    user = models.User.objects.get(id = pk)
    serializer = UserSerializer(instance = user, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['DELETE'])
# def userDelete(request, pk):
#     user = models.User.objects.get(id = pk)
#     user.delete()
#     return Response('Item successfully deleted!')
