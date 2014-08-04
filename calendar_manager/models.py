 #-*- coding: utf-8 -*-
from django.db import models
from user_manager.models import Profile 



class CalendarSettings(models.Model):
        owner=models.ForeignKey(Profile)
        lang=models.CharField(max_length=100)
        timezone= models.CharField(max_length=100)
        email_remind= models.BooleanField()
        sms_remind= models.BooleanField()
        show_weekend= models.BooleanField()
        weekNumbers=models.BooleanField()
        weekNumberTitle=models.CharField(max_length=100)
        defaultView=models.CharField(max_length=100)
        firstDay=models.IntegerField()
        hiddenDays=models.BooleanField()
        defaultTimedEventDuration= models.CharField(max_length=40)
        editable= models.BooleanField() 
        minTime=models.CharField(max_length=40)
        maxTime=models.CharField(max_length=40)
        slotDuration= models.CharField(max_length=40)
        selectable=models.BooleanField()
        allDaySlot=models.CharField(max_length=40)


class Event(models.Model):
      owner=models.ForeignKey(Profile) 
      tiltle=models.CharField(max_length=100)
      starts_at= models.DateTimeField(auto_now_add=False, auto_now=False)
      ends_at= models.DateTimeField(auto_now_add=False, auto_now=False)
      where=models.CharField(max_length=100)
      about= models.CharField(max_length=10000)
      created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
      updated_at= models.DateTimeField(auto_now_add=True, auto_now=True)


