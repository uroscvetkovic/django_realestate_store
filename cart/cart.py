import datetime
from decimal import Decimal
from realestate_store.models import RealEstate

CART_ID = 'CART-ID'

class Cart(object):
    def __init__(self, request):
        self.cart_session = request.session
        cart = self.cart_session.get(CART_ID)
        if not cart:
            cart = self.cart_session[CART_ID] = {}
        self.cart = cart

    def __iter__(self):
        realestates_ids = self.cart.keys()
        realestates = RealEstate.objects.filter(id__in = realestates_ids)
        cartCopy = self.cart.copy()
        for realestate in realestates:
            cartCopy[str(realestate.id)]['realestate'] = realestate
        for item in cartCopy.values():
            item['price'] = Decimal(item['price'])
            item['sum_price'] = item['price']
            yield item


    def __len__(self):
        return sum(1 for item in self.cart.values())

    def full_price(self):
        return sum(float(item['price']) for item in self.cart.values())

    def add(self, realestate):
        realestate_id = str(realestate.id)
        if realestate_id not in self.cart:
            self.cart[realestate_id] = {'full_address':f"{realestate.sity}, {realestate.address}", 'price':str(realestate.price)}
        self.cart_session.modified = True

    def remove(self, realestate):
        realestate_id = str(realestate.id)
        if realestate_id in self.cart:
            del self.cart[realestate_id]
        self.cart_session.modified = True


    def del_from_session(self):
        del self.cart_session[CART_ID]
        self.cart_session.modified = True
