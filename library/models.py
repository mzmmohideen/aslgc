from django.db import models

# Create your models here.
class user(models.Model):
	uname = models.CharField(max_length=50)
	gender = models.CharField(max_length=50)
	uid = models.CharField(max_length=50)
	mobile = models.IntegerField(max_length=20)
	uaddr = models.CharField(max_length=50)

class book(models.Model):
	btitle = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	publisher = models.CharField(max_length=50)
	bid = models.IntegerField(max_length=20)
	quantity = models.CharField(max_length=50)
