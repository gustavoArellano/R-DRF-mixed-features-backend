from django.shortcuts import render 
from django.http import JsonResponse 
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response 
from .serializers import UserSerializer, UserSerializerWithToken, EventSerializer
from . models import User, Event


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'User List': '/user-list/',
        'User Detail View': '/user-detail/<str:pk>/',
        'User Create': '/user-create/',
        'User Update': '/user-update/<str:pk>/',
        'User Delete': '/user-delete/<str:pk>/',
        'EventList': '/event-list/',
        'Event Detail View': '/event-detail/<str:pk>/',
        'Event Create': '/event-create/',
        'Event Update': '/event-update/<str:pk>/',
        'Event Delete': '/event-delete/<str:pk>/'
    }
    return Response(api_urls)

################# USER VIEWS #################
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
    print("THIS IS THE DATA BEING RECIEVED = ", request.data)
    serializer = UserSerializer(instance = user, data = request.data)
    if serializer.is_valid():
        serializer.save()
        print("DATA = ", serializer.data)
        return Response(serializer.data, print("User updated!!!!"))
    print("ERRORS = ", serializer.errors)
    return Response(serializer.errors, print("Update Failed!!!"))

@api_view(['DELETE'])
def userDelete(request, pk):
    user = User.objects.get(id = pk)
    user.delete()
    return Response('User successfully deleted!')


################# EVENT VIEWS #################
@api_view(['POST'])
def eventCreate(request):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    serializer = EventSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, print(serializer.data, "Event created!!"))
    else:
        return Response(serializer.data, print(serializer.errors, "Error in event Create View"))

@api_view(['GET'])
def eventList(request):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    users = User.objects.all()
    events = Event.objects.all()
    serializer = EventSerializer(events, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def eventDetail(request, pk):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    event = Event.objects.get(id = pk)
    print(event)
    serializer = EventSerializer(event, many = False)
    return Response(serializer.data)        

@api_view(['GET'])
def attendingList(request, pk):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    user = User.objects.get(id = pk)
    attending_event = user.users_going_related.all()
    serializer = EventSerializer(attending_event, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def notAttendingList(request, pk):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    user = User.objects.get(id = pk)
    event_not_attending = Event.objects.exclude(users_going = user.id)
    serializer = EventSerializer(event_not_attending, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def joinEvent(request, pk, id):
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    event = Event.objects.get(id = pk)
    user = User.objects.get(id = id)
    event.users_going.add(user)
    return Response(print("JOINED!!!!!!!"))


@api_view(['POST'])
def leaveEvent(request, pk, id): 
    authentication_classes(TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    event = Event.objects.get(id = pk)
    user = User.objects.get(id = id)
    event.users_going.remove(user)
    return Response(print("LEFT!!!!!!!"))