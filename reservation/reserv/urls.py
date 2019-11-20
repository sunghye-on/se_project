
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserv_home, name="resrv_home"),
    path("check/", views.test_reserv_check, name="reserv_check"),
]
