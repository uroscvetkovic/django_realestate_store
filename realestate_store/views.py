from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import RealEstate, Type

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
