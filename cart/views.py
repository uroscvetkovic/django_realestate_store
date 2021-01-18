from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from realestate_store.models import RealEstate
from .cart import Cart
from .form import ButtonForm

@require_POST
def add_to_cart(request, realestate_id):
    cart = Cart(request)
    realestate = get_object_or_404(RealEstate, id = realestate_id)
    cart.add(realestate=realestate)
    return redirect('cart_detail')

@require_POST
def remove_from_cart(request, realestate_id):
    cart = Cart(request)
    realestate = get_object_or_404(RealEstate, id = realestate_id)
    cart.remove(realestate=realestate)
    return redirect('cart_detail')

def f(cart):
    return sum(float(item['price']) for item in cart.values())

def cart_detail(request):
    cart = Cart(request)
    print(cart.cart)
    full_price = f(cart.cart)
    return render(request, 'cart_detail.html', {'cart':cart, 'full_price':full_price})
