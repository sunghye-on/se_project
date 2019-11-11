
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserv_home, name="resrv_home"),
]
