from django.shortcuts import render
from django.http import HttpResponse

import datetime,json


from .models import Greeting, Person



from faker import Factory


dummyjson = ["item1", "item2", "item3"]


def login(nr):
	fake= Factory.create()
	for _ in range(nr):
		Person(first_name = fake.name()).save()



# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'todaytime': now, 'tabledata':login(10)})


# Create your views here.
def tables(request):
    now = datetime.datetime.now()
    return render(request, 'tables.html', {'todaytime': now})

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

