from django.urls import path
from .views import realestate_list, RealEstateDetailView
from . import views

urlpatterns = [
    path('', realestate_list, name='realestate_list'),
    path('<str:name>/', realestate_list, name='realestate_list'),
    path('detail/<int:pk>/', RealEstateDetailView.as_view(), name='realestate_detail')
]
