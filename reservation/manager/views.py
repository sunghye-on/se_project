from django.shortcuts import render, redirect
from login.models import User, Restaurant
from django.core.paginator import Paginator
from reserv.models import *
from login.models import *
from .models import *

from point.models import *

# Create your views here.
def m_home(request) :
    return render(request, 'manager/home.html')
# 매장관리 -> 테이블 수정 누르면 admin의 수정 페이지 이동
def r_edit(request, list_id):
    return redirect('/admin/manager/table/'+str(list_id)+'/change/')
# 유저관리 -> 수정 누르면 admin의 수정 페이지 이동
def u_edit(request, list_id):
    return redirect('/admin/login/user/'+str(list_id)+'/change/')
# 예약관리 -> 수정 누르면 admin의 수정 페이지 이동
def rser_edit(request, list_id):
    return redirect('/admin/reserv/reservation/'+str(list_id)+'/change/')
def table_add(request):
    return redirect('/admin/manager/table/add/')
def m_reserv(request):
    #예약 리스트를 가져옴 
    list = Reservation.objects
    list_all = Reservation.objects.all().order_by('-reservation_time')
    paginator = Paginator(list_all,6)
    page1 = request.GET.get('page')
    posts = paginator.get_page(page1)
    return render(request, 'manager/reserv.html',{'list':list, 'posts':posts})
#테이블 정보 가져옴
def m_restaurant(request):
    list = Table.objects
    list_all = Table.objects.all().order_by('table_num')
    paginator = Paginator(list_all,6)
    page1 = request.GET.get('page')
    posts = paginator.get_page(page1)
    return render(request, 'manager/restaurant.html', {'list':list , 'posts':posts})
def getpage(request):
    num = request.GET['pagenum']
    return redirect('/manager/page/reserv/?page='+num)

def delete(request, list_id):
    #삭제 함수 제작
    res = Reservation.objects.get(id=list_id)
    res.delete()
    return redirect('/manager/page/reserv')
def m_user(request):

    list = NormalUser.objects and User.objects 

    list = NormalUser.objects and User.objects
    list_all = NormalUser.objects.all() and User.objects.all()
    paginator = Paginator(list_all,6)
    page1 = request.GET.get('page')
    posts = paginator.get_page(page1)
    return render(request, 'manager/user.html', {'list':list , 'posts':posts})
    