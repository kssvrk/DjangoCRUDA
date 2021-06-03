from django.contrib import admin

# Register your models here.
from nrscnetra.models import System

class SystemAdmin(admin.ModelAdmin):
    pass
admin.site.register(System, SystemAdmin)