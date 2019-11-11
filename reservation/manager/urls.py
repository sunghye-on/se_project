
from django.urls import path
from . import views

urlpatterns = [
    path('', views.m_home, name='m_home'),
    path('accept/managing/', views.m_accept, name='m_accept'),
    path('reserv/', views.m_reserv, name = 'm_reserv'),
    path('restaurant/', views.m_restaurant, name = 'm_restaurant'),
    path('getpage/', views.getpage, name = "getpage"),
]
