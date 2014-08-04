# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Profile,Application,Tab,Page,Footer
from serializer import ProfileSerializer,TabSerializer,FooterSerializer
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect
from django.http import HttpResponse,HttpRequest
from forms import  ConnexionForm 
from django.core.urlresolvers import reverse
import RyadEssalihine 
from django.contrib.auth.decorators import login_required




@api_view(['POST'])
def register(request):
     pass

@api_view(['GET'])
def user_list(request):
    profiles=Profile.objects.all()
    serializer=ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def  user_get(request):
    try:
        profiles = Profile.objects.get(user_id=request.user.id)

    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=ProfileSerializer(profiles)
    return Response(serializer.data)


@api_view(['GET'])
def tabs_list(request):
    tabs=Tab.objects.all()
    serializer= TabSerializer(tabs,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def footers_list(request):
    footers=Footer.objects.all()
    serializer=FooterSerializer(footers,many=True)
    return Response(serializer.data)



