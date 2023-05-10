from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from Kite.models import Product
from .models import Cart, Cartitem

# Create your views here.


def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save(),
    try:
        cart_item=Cartitem.objects.get(product=product,cart=cart)
        if cart_item.Qty < cart_item.product.stock:
            cart_item.Qty += 1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item=Cartitem.objects.create(
            product=product,
            Qty=1,
            cart=cart
        )
        cart_item.save()
    return redirect('Cart:cart_detail')

def cart_detail(request,total=0,counter=0,cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_item=Cartitem.objects.filter(cart=cart,active=True)
        for cart_items in cart_item:
            total += (cart_items.product.price * cart_items.Qty)
            counter += cart_items.Qty
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_item=cart_item,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=Cartitem.objects.get(product=product,cart=cart)
    if cart_item.Qty >1:
        cart_item.Qty -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cart:cart_detail')

def full_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=Cartitem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('Cart:cart_detail')





