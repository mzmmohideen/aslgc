from django.db import models

# Create your models here.
class user(models.Model):
	userid = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	contact_No = models.IntegerField(max_length=20)
	Address = models.CharField(max_length=50)
	
	
