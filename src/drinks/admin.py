from django.contrib import admin

# Register your models here.

from .models import DrinkInfo

admin.site.register(DrinkInfo)