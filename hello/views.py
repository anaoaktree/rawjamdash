from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import datetime,json, random
from hello.models import SubUser

from django.contrib.auth.models import User

#user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#user.save()
#u = User.objects.get(username='john')
#u.set_password('new password')
#u.save()

# gets the current date
now = datetime.datetime.now()

def login(request):
	return render(request, 'login.html', {})

def login(request):                                                                                                                         
52     if request.method == 'POST':                                                                                                            
53         request.session.set_test_cookie()                                                                                                   
54         login_form = AuthenticationForm(request, request.POST)                                                                              
55         if login_form.is_valid():                                                                                                           
56             if request.is_ajax:                                                                                                             
57                 user = django_login(request, login_form.get_user())                                                                         
58                 if user is not None:                                                                                                        
           else:                                                                                                                               
61                return HttpResponseForbidden() # catch invalid ajax and all non ajax**                                        
60     else:                                                                                                                                   
61         login_form = AuthenticationForm(request)                                                                                            
62                                                                                                                                             
63     c = Context({                                                                                                                           
64         'next': request.REQUEST.get('next'),                                                                                                
65         'login_form': login_form,                                                                                                           
66         'request':request,                                                                                                                  
67     })                                                                                                                                      
68     return render_to_response('login.html', c, context_instance=RequestContext(request))

# Fist dashboard page
@login_required(redirect_field_name='index')
def index(request):
	#if True:
#		return redirect("login")
	return render(request, 'index.html', {'todaytime': now})


# Loads the table pages
def tables(request):
	return render(request, 'tables.html', {'todaytime': now, 'tabledata': SubUser.objects.filter(gender="M"),'lastweek': SubUser.objects.filter(when=1),'over60': SubUser.objects.filter(age__gt=60)})


#Gets assync data to fill in the big table
def bigTable(request):
    return render(request, 'bigTable.html', {'todaytime': now, 'allUsers':SubUser.objects.all()})    


# gets the values for the charts
def getCounter(request):
	male = SubUser.objects.filter(gender="M").count()
	female = SubUser.objects.filter(gender="F").count()
	age0 = SubUser.objects.filter(age__lt=10)
	return JsonResponse({"male":male, "female":female, "age0":age0})


#Gets the total nr of subway users
def getCountAll(request):
	return JsonResponse({"count":SubUser.objects.count()})