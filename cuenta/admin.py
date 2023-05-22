from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta

# Register your models here.

class CuentaAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'apellido', 'username', 'last_login', 'fecha_creacion', 'is_active')
    list_display_links = ('email', 'nombre', 'apellido')
    readonly_fields = ('last_login', 'fecha_creacion')
    ordering = ('-fecha_creacion',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cuenta, CuentaAdmin)