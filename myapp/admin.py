from django.contrib import admin
from .models import UserJsonData,LastAccessData
# Register your models here.

admin.site.register(UserJsonData)
admin.site.register(LastAccessData)
