from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('payments_complete/', views.payments_complete, name='payments_complete'),
    path('realizar_pago/', views.realizar_pago, name='realizar_pago'),
]