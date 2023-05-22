from django.shortcuts import render
from almacen.models import Producto

def home(request):
    productos = Producto.objects.filter(is_available=True)

    context = {
        'productos': productos,
    }

    return render(request, 'home.html', context)