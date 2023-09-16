from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'phone_number', 'datetime_created', 'is_paid')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    fields = ('order', 'product', 'quantity', 'price')
