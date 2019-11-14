
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
