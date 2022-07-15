from django.db import models
from django.conf import settings

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    
    