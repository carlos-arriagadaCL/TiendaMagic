from django.contrib import admin
from .models import Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'slug')

admin.site.register(Categoria)