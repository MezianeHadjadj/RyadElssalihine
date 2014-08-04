#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def calendar(request):
    return render(request ,'backend/calendar/calendar.html')
