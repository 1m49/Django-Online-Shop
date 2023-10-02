from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import OrderForm


@login_required
def order_create_view(request):
    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
        messages.success(request, 'سفارش شما با موفقیت ثبت شد ✅', 'success')

    return render(request, 'orders/order_create.html', context={'form': order_form})
