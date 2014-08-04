from models import Profile ,Phone,Email,Website,Address,Application,Page,Tab,Footer
from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User 



class PhoneSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Phone
            fields=('id','type_number','number','created_at','updated_at')
class EmailSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Email
            fields=('id','email','created_at','updated_at')
class WebsiteSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Website
            fields=('id','website','created_at','updated_at')
class AddressSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Address
            fields=('id','country','state','city','street','postal_code','created_at','updated_at')
class PageSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Page
            fields=('id','name','label','url','icon','about','added_at','last_visit_at')
class ApplicationSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Application
            fields=('id','name','label','url','icon','about','added_at','last_visit_at')

class ProfileSerializer(serializers.ModelSerializer):
    user= serializers.RelatedField(many=False)
    phones= PhoneSerializer(many=True)
    emails= EmailSerializer(many=True)
    websites= WebsiteSerializer(many=True)
    addresses=AddressSerializer(many=True)
    pages=PageSerializer(many=True)
    applications=ApplicationSerializer(many=True) 
    class Meta:
        model = Profile
        fields = ('id', 'user','phones','emails','websites','addresses','pages','applications')




class TabSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Tab
            fields=('id','name','label','url','icon','about')



class FooterSerializer(serializers.ModelSerializer): 
      class Meta:
            model=Footer
            fields=('id','name','label','url','about')