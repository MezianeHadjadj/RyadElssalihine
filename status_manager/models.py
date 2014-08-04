from django.db import models

# Create your models here.
from django.contrib.auth.models import User 
from user_manager.models import Profile





class Status(models.Model):
      content=models.TextField()
      created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
      updated_at= models.DateTimeField(auto_now_add=True, auto_now=True)
      owner=models.ForeignKey(Profile,related_name="status")
