from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank= True)
    
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)


