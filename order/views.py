from django.shortcuts import render
from cart.cart import Cart
from .models import ItemOrder
from .forms import OrderForm

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                ItemOrder.objects.create(order=order, realestate=item['realestate'], price = item['price'])
            cart.del_from_session()
            return render(request, 'created.html', {'order':order})
    else:
        form = OrderForm()
    return render(request, 'create.html', {'cart':cart, 'form': form})
