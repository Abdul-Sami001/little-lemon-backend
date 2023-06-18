from django.contrib import admin
from .models import Menue, Drinks, Drink_Categories, Logger, Booking, Employee

# Register your models here.
admin.site.register(Menue)
admin.site.register(Drinks)
admin.site.register(Drink_Categories)
admin.site.register(Logger)
admin.site.register(Booking)
admin.site.register(Employee)
