#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 



class Profile(models.Model):
      user=models.OneToOneField(User)



class Phone(models.Model):
      type_number= models.CharField(max_length=100)
      number= models.CharField(max_length=20)
      created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
      updated_at= models.DateTimeField(auto_now_add=True, auto_now=True)
      owner=models.ForeignKey(Profile,related_name="phones")

class Email(models.Model):
      email=models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
      updated_at= models.DateTimeField(auto_now_add=True, auto_now=True)
      owner=models.ForeignKey(Profile,related_name="emails")

class Website(models.Model):
      website=models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
      updated_at= models.DateTimeField(auto_now_add=True, auto_now=True)
      owner=models.ForeignKey(Profile,related_name="websites") 

class Address(models.Model):
      country= models.CharField(max_length=100)
      state=models.CharField(max_length=100)
      city=models.CharField(max_length=100)
      street=models.CharField(max_length=500)
      postal_code=models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
      updated_at= models.DateTimeField(auto_now_add=True, auto_now=True)
      owner=models.ForeignKey(Profile,related_name="addresses")

class Application(models.Model):
    name=models.CharField(max_length=100)
    label=models.CharField(max_length=100)
    url=models.CharField(max_length=100) 
    icon=models.CharField(max_length=100) 
    about=models.TextField(null=True)
    added_at=models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="adding date")
    last_visit_at=models.DateTimeField(auto_now_add=True, auto_now=True,verbose_name="last visit date")
    owner=models.ForeignKey(Profile,related_name="applications")  

class Tab(models.Model):
      name=models.CharField(max_length=100)
      label=models.CharField(max_length=100)
      url=models.CharField(max_length=100)
      icon=models.CharField(max_length=100)
      about= models.TextField(null=True)
      

class Page(models.Model):
     name=models.CharField(max_length=100)
     label=models.CharField(max_length=100)
     url=models.CharField(max_length=100)
     icon=models.CharField(max_length=100)
     about=models.CharField(max_length=100)
     added_at=models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="adding date")
     last_visit_at=models.DateTimeField(auto_now_add=True, auto_now=True,verbose_name="last visit date")
     owner=models.ForeignKey(Profile,related_name="pages")


class Footer(models.Model):
      name=models.CharField(max_length=100)
      label=models.CharField(max_length=100)
      url=models.CharField(max_length=100)
      about= models.TextField(max_length=100)