from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Hotel(models.Model):
    hotel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    address = models.TextField()
    image = models.ImageField(upload_to="hotels")   
    vacancy = models.PositiveIntegerField()
     
    

    