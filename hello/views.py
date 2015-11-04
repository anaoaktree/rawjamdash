from django.shortcuts import render
from django.http import HttpResponse

import datetime


from .models import Greeting

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'todaytime': now})


# Create your views here.
def tables(request):
    now = datetime.datetime.now()
    return render(request, 'table.html', {'todaytime': now})

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

