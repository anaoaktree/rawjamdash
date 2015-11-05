from django.shortcuts import render
from django.http import HttpResponse

import datetime,json, random
from hello.models import SubUser
from faker import Factory


fake= Factory.create()


def run():
	for _ in range(100):
		p= fake.simple_profile()
		SubUser(name = p["name"], gender= p["sex"], age = random.randint(0,99), when= random.randint(1,4)).save()




now = datetime.datetime.now()



# Create your views here.
def index(request):
	Person.objects.all().delete()
	return render(request, 'index.html', {'todaytime': now})


# Loads the table pages
def tables(request):
	run()
	return render(request, 'tables.html', {'todaytime': now, 'tabledata': SubUser.objects.filter(gender="M"),'lastweek': SubUser.objects.filter(when=1),'over60': SubUser.objects.filter(age__gt=60)})


#Gets assync data to fill in the big table
def bigTable(request):
    return render(request, 'bigTable.html', {'todaytime': now, 'allUsers':SubUser.objects.all()})    



def getCounter(request):
	male = SubUser.objects.filter(gender="M").count()
	female = SubUser.objects.filter(gender="F").count()
	age0 = SubUser.objects.filter(age__lt=10)
	return JsonResponse({"male":male, "female":female, "age0":age0})


#Gets the total nr of subway users
def getCountAll(request):
	return JsonResponse({"count":SubUser.objects.count()})

# Gets the 
def getCountM(request):
	return JsonResponse({"count":SubUser.objects.filter(gender="M").count()})


def getCountF(request):
	return JsonResponse({"count":SubUser.objects.filter(gender="F").count()})