from django.shortcuts import render, redirect, get_object_or_404
from ecomapp.models import Product
from .models import Cart,Cartitem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def Carts(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def addcart(request,productid):
    product=Product.objects.get(id=productid)
    try:
        cart=Cart.objects.get(cartid=Carts(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cartid=Carts(request))
        cart.save(),
    try:
        cartitem=Cartitem.objects.get(product=product,cart=cart)
        if cartitem.quantity < cartitem.product.stock:
            cartitem.quantity +=1
        cartitem.save()
    except Cartitem.DoesNotExist:
        cartitem=Cartitem.objects.create(product=product,quantity=1,cart=cart)
        cartitem.save()
    return redirect('cart:cartdet')

def cartdet(request,total=0,counter=0,cartitems=None):
    try:
        cart=Cart.objects.get(cartid=Carts(request))
        cartitems=Cartitem.objects.filter(cart=cart,active=True)
        for cartitem in cartitems:
            total +=(cartitem.product.price * cartitem.quantity)
            counter +=cartitem.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cartitems=cartitems,total=total,counter=counter))
def cartdel(request,productid):
    cart=Cart.objects.get(cartid=Carts(request))
    product=get_object_or_404(Product,id=productid)
    cartitem=Cartitem.objects.get(product=product,cart=cart)
    if cartitem.quantity > 1:
        cartitem.quantity -=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cart:cartdet')
def trash(request,productid):
    cart = Cart.objects.get(cartid=Carts(request))
    product = get_object_or_404(Product, id=productid)
    cartitem = Cartitem.objects.get(product=product, cart=cart)
    cartitem.delete()
    return redirect('cart:cartdet')