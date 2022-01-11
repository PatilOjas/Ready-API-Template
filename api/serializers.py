from django.db.models import fields
from rest_framework import serializers
from .models import API_User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = API_User
		fields = '__all__'
	
	def validate(self, data):
		data['name'] = data['name'].strip()
		print(data)
		if not data['name'].isalpha():
			raise serializers.ValidationError("Username must be completely aphabetic with no spaces.")
		
		return data

class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'password', 'email']

	def create(self, validate_data):
		validate_data['password'] = make_password(validate_data['password'])
		return super(AdminSerializer, self).create(validate_data)