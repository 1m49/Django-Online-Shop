from django.contrib import admin
from .models import Product, Comment


# register product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active')


# register comment
@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'body', 'active', 'stars')
