from django.contrib import admin
from .models import Users, Service, Servicer, JOb

# Register your models here.
admin.site.register(Users)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "cost")


admin.site.register(Servicer)

admin.site.register(JOb)
