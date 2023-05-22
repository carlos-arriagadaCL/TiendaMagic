from django.shortcuts import render, get_object_or_404

from carts.models import CartItem
from carts.views import _cart_id
from carts.context_processors import counter
from .models import Producto, Variation
from categoria.models import Categoria
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.

def store(request, category_slug=None):
    categorias = None
    productos = None
    variaciones = None

    if category_slug != None:
        categorias = get_object_or_404(Categoria, slug=category_slug)
        productos = Producto.objects.filter(categoria=categorias, is_available=True)
        paginator = Paginator(productos, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        productos_count = productos.count()
    else:
        productos = Producto.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(productos, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        productos_count = productos.count()

    context = {
        'productos': paged_products,
        'productos_count': productos_count,
        'category_slug': category_slug,
        'categoria': categorias,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Producto.objects.get(categoria__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'counter': counter(request).get('cart_count'),
    }
    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            productos = Producto.objects.order_by('-fecha_creacion').filter(Q(descripcion__icontains=keyword) | Q(nombre__icontains=keyword))
            productos_count = productos.count()

    context = {
        'productos': productos,
        'productos_count': productos_count,
        'keyword': keyword,
    }
    return render(request, 'store/store.html', context)