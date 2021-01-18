from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .models import RealEstate, Type
from cart.cart import Cart
from cart.form import ButtonForm
string = 'stringgg'

def realestate_list(request, name=None):
    type = None
    types = Type.objects.all()
    realestates = RealEstate.objects.filter(available=True)
    if name:
        type = get_object_or_404(Type, name=name)
        realestates = RealEstate.objects.filter(type=type)
    return render(request, 'realestate_list.html',
            {'type':type, 'types':types, 'realestates':realestates})

class RealEstateDetailView(DetailView):
    model = RealEstate
    template_name = 'realestate_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['form'] = ButtonForm()
        return context
