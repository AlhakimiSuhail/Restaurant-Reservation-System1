from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LoginCredentials)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(userReservationInfo)
