from django.contrib import admin
from .models import ItemOrder, Order

class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    raw_id_fileds = ['realestate']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', "name", 'last_name', 'email', 'phone_num', 'date_created', 'payed']
    last_filter = ['payed']
    inlines = [ItemOrderInline] 
