from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Car

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'app/car.html', {})


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(response):
    car_list = Car.objects.order_by("-created_at")
    return render(response, 'app/home.html', {"cars": car_list})


def car(response, id):
    return render(response, 'app/car.html', {"car": Car.objects.get(pk=id)})
