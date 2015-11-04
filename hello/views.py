from django.shortcuts import render
from django.http import HttpResponse

import datetime,json


from .models import Greeting

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

