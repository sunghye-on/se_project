
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserv_home, name="resrv_home"),
    path("check/", views.reserv_check, name="reserv_check"),
    path("modify/", views.test_modify, name="test_modify"),
]
