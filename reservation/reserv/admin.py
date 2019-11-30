from django.contrib import admin
from .models import *
from login.models import *
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Relate_reserv)
