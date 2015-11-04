from django.db import models
from faker import Factory


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)




class Person(models.Model):
	first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #release_date = models.DateField()
    age = models.IntegerField()
    bio = models.CharField(max_length=30)


