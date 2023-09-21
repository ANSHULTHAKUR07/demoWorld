from cart.cart import Cart
from decimal import Decimal


def totalprice(request):
    cart = Cart(request)
    total = sum(Decimal(item['price']) * item['quantity'] for item in cart.cart.values())
    return total

