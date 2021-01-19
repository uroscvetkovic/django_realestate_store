from django.db import models
from realestate_store.models import RealEstate

class Order(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    payed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self): return f'Order {self.id}'

    def get_full_price_of_order(self):
        return sum(item.GetPrice() for item in self.item_order_p.all())

class ItemOrder(models.Model):
    order = models.ForeignKey(Order, related_name='item_order_p',on_delete=models.CASCADE)
    realestate = models.ForeignKey(RealEstate, related_name='item_order_a', on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self): return str(self.id)

    def GetPrice(self): return self.price
