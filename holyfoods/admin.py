from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Shop
from .models import Donut
admin.site.register(Shop)
admin.site.register(Donut)
