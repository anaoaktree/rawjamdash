from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.CharField()


class Person(models.Model):
	firstName = models.CharField(max_length=30)
	#last_name = models.CharField(max_length=30) #release_date = models.DateField()
	#age = models.IntegerField()
	#bio = models.CharField(max_length=30)


