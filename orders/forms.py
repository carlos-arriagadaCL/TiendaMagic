from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion', 'pais', 'ciudad', 'comuna', 'orden_notas']