from distutils.sysconfig import customize_compiler
from re import U
from django.db import models
from Dish.models import Dish
from Customer.models import Customer

# Create your models here.

class Order(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=10)
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null = True)    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.BooleanField() 
       
    

    