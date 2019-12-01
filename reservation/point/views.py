
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
# Create your views here.
from login.models import *

def point(request):
    list = NormalUser.objects 
    list_all = NormalUser.objects.all() 
    paginator = Paginator(list_all,6)
    page1 = request.GET.get('page')
    posts = paginator.get_page(page1)
    return render(request , "point.html", {'list':list , 'posts':posts})

# 매출 포인트 적립
def calPoint(request, list_id):
    user= NormalUser.objects.get(id = list_id)
    mode = request.POST.get('mode')
    money = request.POST.get('money')
   # 모드선택 안하거나 돈이 안들어간경우 
    if (money == "" or mode == str(0)):
        return redirect('/manager/page/point')
    
     # 판매 포인트적립
    if (mode == str(1)):
        point = user.point + int(int(money)*0.1)
        user.point = point 
        user.save()
        return redirect('/manager/page/point')
    
    # 선 입금 포인트적립
    elif (mode == str(2)):
        point = user.point + int(money)
        user.point = point
        user.save()
        return redirect('/manager/page/point')
    
    # 포인트 사용
    elif (mode == str(3)):
        if (user.point < int(money)):
            # 포인트가 더 적음
            return redirect('/manager/page/point')
        user.point = user.point - int(money)
        user.save()
        return redirect('/manager/page/point')
    else :
        return redirect('/manager/page/point')
    




