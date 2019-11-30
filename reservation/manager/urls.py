
from django.urls import path
from . import views

urlpatterns = [
    path('', views.m_home, name='m_home'),
    # path('accept/managing/', views.m_accept, name='m_accept'),
    path('reserv/', views.m_reserv, name = 'm_reserv'),
    path('restaurant/', views.m_restaurant, name = 'm_restaurant'),
    path('user/', views.m_user, name = 'm_user'),
    path('table_add/', views.table_add, name = 'table_add'),
    path('getpage/', views.getpage, name = "getpage"),
    path('delete/<int:list_id>/', views.delete, name ="delete"),
    path('redit/<int:list_id>/', views.r_edit, name ="r_edit"),
    path('uedit/<int:list_id>/', views.u_edit, name ="u_edit"),
    path('rseredit/<int:list_id>/', views.rser_edit, name ="rseredit"),
]
