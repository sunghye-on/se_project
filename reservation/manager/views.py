from django.shortcuts import render, redirect
from login.models import User, Restaurant, Location
from django.core.paginator import Paginator
from reserv.models import *
# Create your views here.
def m_home(request) :
    return render(request, 'manager/home.html')

def m_reserv(request):
    #예약 리스트를 가져옴 
    list = Reservation.objects
    list_all = Reservation.objects.all()
    paginator = Paginator(list_all,3)
    page1 = request.GET.get('page')
    posts = paginator.get_page(page1)
    return render(request, 'manager/reserv.html',{'list':list, 'posts':posts})

def m_restaurant(request):
    return render(request, 'manager/restaurant.html')
def getpage(request):
    num = request.GET['pagenum']
    return redirect('/manager/page/reserv/?page='+num)

def m_accept (request) :
    if request.method == "POST":
        userinfo = User.objects.get(idName=userid)
        userinfo.isManager = True
        userinfo.save()

        request.session['manager'] = True

        restname = request.POST['restName']
        location = request.POST['local']

        local = Location.objects.get(city=location)
        
        rest = Restaurant (
            name = restname,
            location = local,
            user = userinfo
        )

        rest.save()

        return redirect('m_home')
    else :
        return render(request, "manager/accept.html")