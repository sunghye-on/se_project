
from django.contrib import admin
from django.urls import path, include

import point.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('reserv/', include("reserv.urls")),
    path('login/', include('login.urls')),
    path('manager/page/', include('manager.urls')),

    path('manager/page/point' , include('point.urls')),

]
