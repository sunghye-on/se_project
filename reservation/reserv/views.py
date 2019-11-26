from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from login.models import *
from .models import *
from datetime import datetime, date
# Create your views here.

def reserv_home(request) :
    # home화면이 아닌 데이터 입력으로 접속함/세션이 존재함
    if request.method == "POST" and request.session.get('userid') :
        try :
            date = datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M')
            hopping_member = int(request.POST['hopping_member'])
            galp = Restaurant.objects
            galpungs = Restaurant.objects.all()
            # 데이터베이스에 있는 갈풍집 가져옮
            for galpung in galpungs :
                galp = galpung
            
            # 갈풍 집에 현재 수용 중인 인원과 최대 받을 수 있는 인원을 비교하여 예약 가능 불가능을 나눔
            if galp.current_customer != galp.max_customer and galp.current_customer + hopping_member <= galp.max_customer and date > datetime.now() :
                # 예약 객체 생성
                reservation = Reservation (
                    reservation_time = date,
                    people = hopping_member
                )
                
                reservation.save()

                user = User.objects.get(idName = request.session.get('userid'))
                # 현재 로그인된 객체와 예약 객체, 갈풍 객체 하나로 합침
                reservation_relate = Relate_reserv (
                    reservate = reservation,
                    user = user,
                    restaurant = galp
                )
                reservation_relate.save()

                return redirect("reserv_check")

            # 현재 시간보다 이 전 시간을 제외시킴
            elif date <= datetime.now() :
                errmsg = "date error"
                return render(request, "reserv/reservate.html", {'errmsg' : errmsg})
            # 전체 가능 예약 인원과, 현재 인원에 대해서 초과된 인원 넘겨줌
            elif galp.current_customer + hopping_member >= galp.max_customer :
                fully_customer = galp.max_customer + galp.current_customer
                errmsg = "Full reservation customer" + fully_customer
                return render(request, "reserv/reservate.html", {"errmsg" : errmsg})
            # 알 수 없는 오류 / 사용자의 잘못된 form 입력
            else :
                errmsg = "Please write right application"
                return render(request, "reserv/reservate.html", {"errmsg" : errmsg})
        except :
            errmsg = "error"
            return render(request, "reserv/reservate.html", {"errmsg" : errmsg})

    return render(request, 'reserv/reservate.html')

# 예약이 얼만큼 됐는지 확인하는 페이지 접근
def reserv_check(request) :
    user = get_object_or_404(User, idName = request.session.get('userid'))
    relates = Relate_reserv.objects.filter(user=user).order_by()
    list_relate = []
    for relate in relates :
        if relate.reservate.reservation_time > timezone.now() :
            list_relate.append(relate.reservate)
    context = {"reservation" : list_relate, "user" : user}
    return render(request, "reserv/reservation_check.html", context)

#def reserv_modify(request, pk) :
    #return render(request, "reserv/reserv_home.html")


def reserv_modify_render(request, pk) :
    reservation = get_object_or_404(Reservation, pk=pk)

    context = {"reservation" : reservation}
    return render(request, "reserv/reserv_modify.html", context)

def reserv_modify(request, pk) :
    # year_month = request.POST["date"]
    # time = request.POST["time"]
    
    
    date = datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M')
    people = int(request.POST["many"])
    
    reservation = get_object_or_404(Reservation, pk=pk)
    relete = get_object_or_404(Relate_reserv, reservate=reservation)
    galp = relete.restaurant

    try :
        reservation.reservation_time = date
        reservation.people = people
        # 현재 시간보다 이 전 시간을 제외시킴
        if date <= datetime.now() :
            errmsg = "date error"
            return render(request, "reserv/reservate.html", {'errmsg' : errmsg})
        # 전체 가능 예약 인원과, 현재 인원에 대해서 초과된 인원 넘겨줌
        elif galp.current_customer + hopping_member >= galp.max_customer :
            fully_customer = galp.max_customer + galp.current_customer
            errmsg = "Full reservation customer" + fully_customer
            return render(request, "reserv/reservate.html", {"errmsg" : errmsg})
        # 알 수 없는 오류 / 사용자의 잘못된 form 입력
        else :
            errmsg = "Please write right application"
            return render(request, "reserv/reservate.html", {"errmsg" : errmsg})
    except :
        return redirect("reserv_modify", id=pk)

    reservation.save()

    return redirect("resrv_home")
