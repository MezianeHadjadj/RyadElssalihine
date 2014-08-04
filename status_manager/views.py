# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from models import Status
from serializer import StatusSerializer 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from user_manager.models import Profile 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from datetime import datetime



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@login_required
def status_show(request):
	return render(request,'backend/status/status_show.html')


@api_view(['GET'])
def status_list(request):
   
    status_list=Status.objects.filter(owner_id=request.user.profile.id).order_by('-created_at')
    serializer=StatusSerializer(status_list,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def status_add(request):
         data = JSONParser().parse(request)
         status_object=Status(content=data["content"],owner=request.user.profile)
         status_object.save()
         serializer=StatusSerializer(status_object)
         if serializer:
            return JSONResponse(serializer.data, status=201)
         return JSONResponse(serializer.errors, status=400)