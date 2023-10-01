from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['user', 'first_name', 'last_name', 'phone_number', 'order_notes']
    list_display = ['user', 'phone_number', 'order_notes']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    fields = ['order', 'product', 'quantity', 'price']
