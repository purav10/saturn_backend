from django.db import models
from Hotel.models import Hotel

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=10)
    isVeg = models.BooleanField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="dishes")    
    

    