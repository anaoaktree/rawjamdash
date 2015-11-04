from django.shortcuts import render
from django.http import HttpResponse

import datetime,json, random


from hello.models import  Person, SubUser

import hello.loadData



from faker import Factory


fake= Factory.create()


def run():
	for _ in range(10):
		p= fake.simple_profile()

		Person(firstName = p["name"]).save()
		SubUser(name = p["name"], gender= p["sex"], age = random.randint(0,99), when= random.randint(1,4)).save()






now = datetime.datetime.now()

# Create your views here.
def index(request):
	Person.objects.all().delete()
	return render(request, 'index.html', {'todaytime': now})


# Create your views here.
def tables(request):
	run()
	return render(request, 'tables.html', {'todaytime': now})



def bigTable(request):
    return render(request, 'bigTable.html', {'todaytime': now, 'allUsers':SubUser.objects.all()})    


def getCountAll(request):
	return JsonResponse({"count":Person.objects.count()})


def getCountM(request):
	return JsonResponse({"count":SubUser.objects.filter(gender="M").count()})


def getCountF(request):
	return JsonResponse({"count":SubUser.objects.filter(gender="F").count()})