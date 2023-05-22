from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from almacen.models import Producto, Variation
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user # obtener el usuario actual
    product = Producto.objects.get(id=product_id) # obtener el producto
    # si el usuario esta autenticado
    if current_user.is_authenticated:
        product_variation = [] # lista de variaciones
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(
                        product = product,
                        variation_category__iexact = key,
                        variation_value__iexact = value,
                    )
                    product_variation.append(variation)
                except:
                    pass

        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, user=current_user)
            existing_variation_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                existing_variation_list.append(list(existing_variation))
                id.append(item.id)

            if product_variation in existing_variation_list:
                # aumentar la cantidad
                index = existing_variation_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                # crear un nuevo item
                item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    user = current_user
                )
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                user = current_user
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')
    # si el usuario no esta autenticado
    else:
        product_variation = [] # lista de variaciones
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(
                        product = product,
                        variation_category__iexact = key,
                        variation_value__iexact = value,
                    )
                    product_variation.append(variation)
                except:
                    pass
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request)) # obtener el carrito usando el id de la sesion
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists() # verificar si el item del carrito existe
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, cart=cart) # obtener el item del carrito

            existing_variation_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                existing_variation_list.append(list(existing_variation))
                id.append(item.id)

            if product_variation in existing_variation_list:
                # aumentar la cantidad
                index = existing_variation_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                # crear un nuevo item
                item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cart
                )
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')

def remove_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Producto, id=product_id) # obtener el producto
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request)) # obtener el carrito usando el id de la sesion
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id) # obtener el item del carrito

        if cart_item.quantity > 1:
            cart_item.quantity -= 1 # disminuir la cantidad
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
    product = get_object_or_404(Producto, id=product_id) # obtener el producto
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # obtener el carrito usando el id de la sesion
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id) # obtener el item del carrito
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request)) # obtener el carrito usando el id de la sesion
            cart_items = CartItem.objects.filter(cart=cart, is_active=True) # obtener los items del carrito
        for cart_item in cart_items:
            total += (cart_item.product.precio * cart_item.quantity) # obtener el total
            quantity += cart_item.quantity # obtener la cantidad
        tax = (19 * total)/100 # obtener el impuesto
        tax = round(tax)
        grand_total = total + tax # obtener el total con impuesto
    except ObjectDoesNotExist:
        pass # solo ignorar

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True) # obtener los items del carrito

        for cart_item in cart_items:
            total += (cart_item.product.precio * cart_item.quantity) # obtener el total
            quantity += cart_item.quantity # obtener la cantidad
        tax = (19 * total)/100 # obtener el impuesto
        tax = round(tax)
        grand_total = total + tax # obtener el total con impuesto
    except ObjectDoesNotExist:
        pass # solo ignorar

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/checkout.html', context)