from django.contrib import admin

# Register your models here.
from nrscnetra.models import System,JobDef,Job

class SystemAdmin(admin.ModelAdmin):
    pass
class JobDefAdmin(admin.ModelAdmin):
    pass
class JobAdmin(admin.ModelAdmin):
    pass
admin.site.register(System, SystemAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobDef, JobDefAdmin)