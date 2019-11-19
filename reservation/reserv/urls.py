
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserv_home, name="resrv_home"),
<<<<<<< HEAD
    path("check/", views.test_reserv_check, name="reserv_check"),
=======
    path("check/", views.reserv_check, name="reserv_check"),
>>>>>>> 04175478770fd5d5c89c7aab388674618ab0ab77
]
