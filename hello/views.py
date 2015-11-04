from django.shortcuts import render
from django.http import HttpResponse

import datetime,json


from .models import Greeting, Person



from faker import Factory


dummyjson = ["Admin"]
fake= Factory.create()



def login(nr):
	fake= Factory.create()
	for _ in range(nr):
		dummyjson.append(fake.name())
		#Person(first_name = fake.name()).save()



# Create your views here.
def index(request):
    now = datetime.datetime.now()
    login(20)
    return render(request, 'index.html', {'todaytime': now, 'tabledata':dummyjson})


# Create your views here.
def tables(request):
    now = datetime.datetime.now()
    allUsers[fake.name() for _ in range(500)]
    return render(request, 'tables.html', {'todaytime': now, 'allUsers':allUsers})

def db(request):
	fake= Factory.create()
	for _ in range(nr):
		Person(first_name = fake.name()).save()
	greetings = Person.objects.all()
	return render(request, 'db.html', {'greetings': greetings})

