from django.contrib import admin
from django.urls import path,include
from . import views

from Customer.models import Customer

urlpatterns = [
    
    path('register/', views.register),
    path('login/', views.login_user),
   
]
