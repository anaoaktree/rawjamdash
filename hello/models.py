from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)





class Game(models.Model):
	pass


class Player(models.Model):
	pass