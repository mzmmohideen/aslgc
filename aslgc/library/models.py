from django.db import models

# Create your models here.
class user(Models.model):
	username = models.Charfield(max_length=50)
	gender = models.Charfield(max_length=50)
	u_id = models.Charfield(max_length=50)
	mobile_no = models.Integerfield(max_length=20)
	address = models.Charfield(max_length=50)

class book(Models.model):
	btitle = models.Charfield(max_length=50)
	author = models.Charfield(max_length=50)
	publisher = models.Charfield(max_length=50)
	bid = models.Integerfield(max_length=20)
	quantity = models.Charfield(max_length=50)
