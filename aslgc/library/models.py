from django.db import models

# Create your models here.
class user(Models.model):
	userid = models.Charfield(max_length=50)
	username = models.Charfield(max_length=50)
	contact_No = models.Integerfield(max_length=20)
	Address = models.Charfield(max_length=50)
	
