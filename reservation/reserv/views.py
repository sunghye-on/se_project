from django.shortcuts import render

# Create your views here.

def reserv_home(request) :
    return render(request, 'reserv/reservate.html')