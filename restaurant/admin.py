from django.contrib import admin

# Register your models here.
from restaurant.models import Booking, MenuItem

admin.site.register(Booking)
admin.site.register(MenuItem)