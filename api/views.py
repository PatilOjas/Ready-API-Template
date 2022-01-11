from django.contrib.messages.constants import INFO
from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer, AdminSerializer
from .models import API_User


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = API_User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Register': '/create/',
		'List': '/list/',
	}

	return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
	users = API_User.objects.all()
	serializer = UserSerializer(users, many=True)
	
	return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
	serializer = UserSerializer(data=request.data)
	print(request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	
	elif request.data['mobile'][0] != '+' or len(request.data['mobile']) != 13 or not request.data['mobile'][1:].isdecimal():
		return Response({"message": "Make sure you are entering mobile number with country code without any spaces e.g. +919876543210"})
	
	else:
		return Response({"message": "You are already a registered user."})

# @api_view(['POST'])
# def register(request):
# 	serializer = AdminSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()
# 		return Response(serializer.data)


	