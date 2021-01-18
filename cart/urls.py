from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:realestate_id>', add_to_cart, name='add_to_cart'),
    path('remove/<int:realestate_id>', remove_from_cart, name='remove_from_cart')
]
