from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


# Product Comment
class Comment(models.Model):
    PRODUCT_START = [
        ('1', 'خیلی بد'),
        ('2', 'بد'),
        ('3', 'معمولی'),
        ('4', 'خوب'),
        ('5', 'خیلی خوب'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name='نظر شما')
    stars = models.CharField(max_length=10, choices=PRODUCT_START , verbose_name='امتیاز')
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} , {self.body[:30]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
