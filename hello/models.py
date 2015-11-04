from django.db import models


# Create your models here.

class Person(models.Model):
	firstName = models.CharField(max_length=30,db_tablespace="indexes")
	

class SubUser(models.Model):
	GEN = (("M","Male"),("F", "Female"))
	name = models.CharField(max_length=30,db_tablespace="indexes")
	gender = models.CharField(max_length=1, choices=GEN)
	age = models.IntegerField()
	when = models.IntegerField()

