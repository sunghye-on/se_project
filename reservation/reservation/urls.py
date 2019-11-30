
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
import point.views
=======

>>>>>>> c6a05983a5e4fb87bfa07f922ce9abae897ba62b
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('reserv/', include("reserv.urls")),
    path('login/', include('login.urls')),
    path('manager/page/', include('manager.urls')),
<<<<<<< HEAD
    path('manager/page/point' , include('point.urls')),
=======
>>>>>>> c6a05983a5e4fb87bfa07f922ce9abae897ba62b
]
