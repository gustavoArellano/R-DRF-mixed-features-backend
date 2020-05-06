from django.shortcuts import render 
from django.http import JsonResponse 
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response 
from .serializers import UserSerializer, UserSerializerWithToken
from . models import User


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
    users = User.objects.all()
    serializer = UserSerializer(users, many = True) 
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    user = User.objects.get(id = pk)
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def userUpdate(request, pk):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    user = User.objects.get(id = pk)
    serializer = UserSerializer(instance = user, data = request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response(serializer.data, print("User updated!!!!"))
    return Response(serializer.errors, print("Update Failed!!!"))

# @api_view(['DELETE'])
# def userDelete(request, pk):
#     user = User.objects.get(id = pk)
#     user.delete()
#     return Response('Item successfully deleted!')
