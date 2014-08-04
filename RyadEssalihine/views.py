#-*- coding: utf-8 -*-

from django.shortcuts import render
from user_manager.models import Tab ,Application,Page,Footer 
from django.contrib.auth.decorators import login_required
from forms import  ConnexionForm 
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect
from django.http import HttpResponse,HttpRequest
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

def home_frontend(request):
   return render(request, 'frontend/base-frontend.html')
     

def welcome(request):
   form=ConnexionForm()
   return render(request, 'frontend/user/welcome.html',locals())  

#@api_view(['GET','POST'])
def logine(request):
    error=False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            user= authenticate(username=username,password=password)
            if user :
                login(request,user)
                username=user.username
                return redirect(home_backend,username)        
            else :
                error=True

    return redirect(home_frontend) 

def logoute(request):
    logout(request)
    return redirect(reverse(home_frontend))
    
@login_required
def home_backend(request,username):
     
    return render(request,'backend/base-backend.html') 
    