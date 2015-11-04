from django.db import models


# Create your models here.

class Person(models.Model):
	firstName = models.CharField(max_length=30,db_tablespace="indexes")
	userName = models.CharField(max_length=10,db_tablespace="indexes")
	#last_name = models.CharField(max_length=30) #release_date = models.DateField()
	#age = models.IntegerField()
	#bio = models.CharField(max_length=30)


