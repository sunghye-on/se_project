
from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.sign_in, name='sign'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
