from django.db import models


# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=30,db_tablespace="indexes")
	#last_name = models.CharField(max_length=30) #release_date = models.DateField()
	#age = models.IntegerField()
	#bio = models.CharField(max_length=30)


