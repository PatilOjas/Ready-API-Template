from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class API_User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, null=False, blank=False)
	mobile = PhoneNumberField(unique=True, null=False, blank=False)
	timestamp = models.DateTimeField(auto_now=True)


	def __str__(self) -> str:
		return self.name