from django.shortcuts import render
from django.http import HttpResponse

import datetime,json


from hello.models import  Person



from faker import Factory



now = datetime.datetime.now()

# Create your views here.
def index(request):
    return render(request, 'index.html', {'todaytime': now})


# Create your views here.
def tables(request):
    return render(request, 'tables.html', {'todaytime': now})



def bigTable(request):
    return render(request, 'bigTable.html', {'todaytime': now, 'allUsers':Person.objects.all()})    


def getCountAll(request):
	return JsonResponse({"count":Client.objects.count()})


def getCountM(request):
	return JsonResponse({"count":Client.objects.filter(gender="M").count()})


def getCountF(request):
	return JsonResponse({"count":Client.objects.filter(gender="F").count()})