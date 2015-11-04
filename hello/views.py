from django.shortcuts import render
from django.http import HttpResponse

import datetime,json


from .models import Greeting, Player, Game

from django_faker import Faker


# this Populator is only a function thats return a django_faker.populator.Populator instance
# correctly initialized with a faker.generator.Generator instance, configured as above
populator = Faker.getPopulator()

from myapp.models import Game, Player
populator.addEntity(Game,5)
populator.addEntity(Player,10)

insertedPks = populator.execute()




dummyjson = ["item1", "item2", "item3"]



# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'todaytime': now, 'tabledata':dummyjson})


# Create your views here.
def tables(request):
    now = datetime.datetime.now()
    return render(request, 'tables.html', {'todaytime': now})

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

