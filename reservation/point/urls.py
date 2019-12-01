
from django.urls import path
from . import views

urlpatterns = [

    path('', views.point , name = "point"),
    path('calPoint/<int:list_id>/', views.calPoint , name = "calPoint"),


]
