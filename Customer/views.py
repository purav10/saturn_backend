from ctypes import addressof
from email import message
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from Customer.models import Customer
from django.contrib.auth import authenticate, login , logout


# Create your views here.
@csrf_exempt
def register(request,   *args, **kwargs):
    message = "User successfully registered"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if Customer.objects.filter(user=user).exists():
                message = "User already exists"
            else:
                customer = Customer(user = user, address = address, phone = phone, name = name)
                customer.save()
            return JsonResponse({"message": message})
        user = User.objects.create_user(username = username, password = password)
        customer = Customer(user = user, address = address, phone = phone, name = name)
        customer.save()
        response = JsonResponse({"message": message})
        return JsonResponse({"message": message})
    
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and Customer.objects.filter(user=user).exists():         
            login(request,user)
            message = "Login successful"
            return JsonResponse({"message": message})     
                   
        else :
            message = "Invalid username or password"
            return JsonResponse({"message": message})
        
@csrf_exempt
def logout_user(request):
    logout(request)
    message = "Logout successful"
    return JsonResponse({"message": message})