import datetime
from django.shortcuts import render, redirect
from carts.models import CartItem
from .models import Order
from .forms import OrderForm
from transbank.webpay.transaccion_completa.transaction import *
from transbank.common.integration_type import *
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def payments(request):
    return render(request, 'orders/payments.html')

@csrf_exempt
def realizar_pago(request):
    if request.method == 'POST':
        buy_order = request.POST['buy_order']
        session_id = request.POST['session_id']
        amount = request.POST['amount']

        # URL de la API de Transbank Webpay para ambiente de integración
        url = 'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.0/transactions'

        # Datos de la transacción
        payload = {
            'buy_order': buy_order,
            'session_id': session_id,
            'amount': amount,
            'return_url': 'http://127.0.0.1:8000/orders/payments_complete/'
        }

        # Headers requeridos
        headers = {
            'Tbk-Api-Key-Id': '597055555532',
            'Tbk-Api-Key-Secret': '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
            'Content-Type': 'application/json'
        }

        # Realizar la solicitud POST a la API de Transbank
        response = requests.post(url, json=payload, headers=headers, verify=True)

        # Obtener la respuesta
        if response.status_code == 200:
            respuesta = response.json()

            # Aquí puedes procesar la respuesta de la API
            return redirect(respuesta['url']+f'?token_ws={respuesta["token"]}')
        else:
            return render(request, 'orders/payments.html')

@csrf_exempt
def payments_complete(request):
    return render(request, 'orders/payments_complete.html')

def place_order(request, total=0, quantity=0):
    current_user = request.user
    # Si el recuento de carritos es cero, redirija de nuevo a la tienda
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.precio * cart_item.quantity) # obtener el total
        quantity += cart_item.quantity # obtener la cantidad
        tax = (19 * total)/100 # obtener el impuesto
        tax = round(tax)
    grand_total = total + tax # obtener el total con impuesto

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.nombre = form.cleaned_data['nombre']
            data.apellido = form.cleaned_data['apellido']
            data.telefono = form.cleaned_data['telefono']
            data.email = form.cleaned_data['email']
            data.direccion = form.cleaned_data['direccion']
            data.pais = form.cleaned_data['pais']
            data.ciudad = form.cleaned_data['ciudad']
            data.comuna = form.cleaned_data['comuna']
            data.orden_notas = form.cleaned_data['orden_notas']
            data.total_orden = grand_total
            data.tax = tax
            data.ip_address = request.META.get('REMOTE_ADDR')

            data.save()
            # Generar numero de orden
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime('%Y%m%d')
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }
            return render(request, 'orders/payments.html', context)
    else:
        return redirect('checkout')