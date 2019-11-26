
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path("find/password/", views.find_pwd, name="find_pwd"),
    path('find/password/change/', views.change_pwd, name="change_pwd"),    
]
