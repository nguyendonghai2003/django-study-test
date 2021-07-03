from django.contrib import admin
from .models import Machine, Mold, Product, Dailyproduction
# Register your models here.

admin.site.register(Machine)
admin.site.register(Mold)
admin.site.register(Product)
admin.site.register(Dailyproduction)