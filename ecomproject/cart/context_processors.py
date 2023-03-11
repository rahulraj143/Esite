from .models import Cart,Cartitem
from .views import Carts

def counter(request):
    itemcount=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cartid=Carts(request))
            cartitem=Cartitem.objects.all().filter(cart=cart[:1])
            for cartitem in cartitem:
                itemcount += cartitem.quantity
        except Cart.DoesNotExist:
            itemcount = 0
    return dict(itemcount=itemcount)
            