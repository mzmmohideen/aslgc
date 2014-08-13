from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
	user = models.OneToOneField(User)
	uname = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	uid = models.CharField(max_length=50,unique = True)
	mobile = models.CharField(max_length=30)
	uaddr = models.CharField(max_length=100)

class book(models.Model):
	btitle = models.CharField(max_length=50)
	category = models.CharField(max_length=50)	
	author = models.CharField(max_length=50)
	publisher = models.CharField(max_length=50)
	bid = models.CharField(max_length=20,unique = True)
	quantity = models.IntegerField(max_length=50)

class booklend(models.Model):
	user = models.ForeignKey('user')	
	book = models.ForeignKey('book')
	status = models.CharField(max_length=50)			
	doi = models.DateTimeField(max_length=50)
	dor = models.DateTimeField(max_length=50)


