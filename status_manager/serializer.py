from models import Status
from django.forms import widgets
from rest_framework import serializers






class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id','content','created_at','updated_at','owner')



