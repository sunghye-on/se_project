from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .models import *

# Create your views here.

def sign_up (request) :
    if request.method == "POST" :
        userid = request.POST["id"]
        password = request.POST["pwd"]
        # city = request.POST["city"]
        # local = Location.objects.get(city=city)
        nickname = request.POST["nickname"]
        phone = request.POST["phone_number"]
        checkpwd = request.POST["checkpwd"]

        if User.objects.filter(idName=userid) :
            errMsg = "이미 존재하는 아이디입니다."
            return render(request, "login/signup.html", {"errMsg" : errMsg})

        if checkpwd != password :
            errMsg = "잘못된 패스워드를 입력했습니다."
            return redirect("home", errMsg)

        user = User (
            idName = userid,
            password = password,
            nickName = nickname,
            # location = local,
            phoneNumber = phone
        )

        user.save()
        return render(request, "login/login.html")
    else :
        return render(request, "login/signup.html")

def logout(request) :
    if request.session.get('userid') :
        request.session['userid'] = None
        request.session['manager'] = None
        return redirect("home")
    else :
        return redirect("home")

def login(request) :
    if request.method == "POST" and request.session.get('userid') == None :
        id = request.POST["id"]
        pwd = request.POST["pwd"]
#                                     컨태인을 없애 버그 픽스
        user = None
        us = User.objects.filter(idName=id, password=pwd)

        for u in us :
            user = u
        
        print(user)
        if user :
            request.session['userid'] = user.idName
            request.session['manager'] = user.isManager
            return redirect("home")
        else :
            errMsg = "로그인 실패"
            return render(request, "login/login.html", {"errMsg" : errMsg})

    elif request.session.get('userid') :
        errMsg = "이미 로그인 중"
        return redirect("login", errMsg)
    else :
        return render(request, "login/login.html")