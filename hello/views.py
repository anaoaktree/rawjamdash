from django.shortcuts import render
from django.http import HttpResponse

import datetime,json


from .models import Greeting, Person



from faker import Factory


dummyjson = ["Admin"]
fake= Factory.create()




now = datetime.datetime.now()

def login(nr):
	fake= Factory.create()
	for _ in range(nr):
		dummyjson.append(fake.name())
		#Person(first_name = fake.name()).save()


def bigTable(request):
    allUsers = [fake.name() for _ in range(500)]
    return render(request, 'bigTable.html', {'todaytime': now, 'allUsers':allUsers})

# Create your views here.
def index(request):
    login(20)
    return render(request, 'index.html', {'todaytime': now, 'tabledata':dummyjson})


# Create your views here.
def tables(request):
    return render(request, 'tables.html', {'todaytime': now})

def db(request):
	for _ in range(10):
		Person(firstName = fake.name()).save()
	greetings = Person.objects.all()
	return render(request, 'db.html', {'greetings': greetings})

