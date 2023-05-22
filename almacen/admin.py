from django.contrib import admin
from .models import Producto, Variation

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'fecha_modificacion', 'is_available')
    prepopulated_fields = {'slug': ('nombre',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Variation, VariationAdmin)