from django.shortcuts import render , redirect
from login.models import *
from reserv.models import *


# Create your views here.
def home(request):
    Foods = Menu.objects.all()
    rest = Restaurant.objects.get(name="갈풍집")
    food = Food.objects.get(food='마늘갈비살')
    print(food.photo)
    context = {"foods" : Foods, "Rest" : rest, 'site' : True}
    
    return render(request, "main/home.html", context)
