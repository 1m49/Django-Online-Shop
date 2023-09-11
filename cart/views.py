from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _
from django.contrib import messages

from .cart import Cart
from products.models import Product
from .forms import AddToCartProductForm


def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', {'cart': cart})


# add product to cart
@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

        messages.success(request, _('Product added successfully '), 'success')

        return redirect('cart:cart_detail')


# remove product from cart
def remove_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)

    cart.remove(product)

    messages.success(request, _('Product removed successfully '), 'success')

    return redirect('cart:cart_detail')
