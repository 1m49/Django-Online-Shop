from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    title = models.CharField(_('title'), max_length=150)
    short_description = models.CharField(_('short description'), max_length=500, blank=True)
    description = RichTextUploadingField(_('description of product'))
    image = models.ImageField(_('product picture'), upload_to='product/product_pic', blank=True)
    old_price = models.PositiveIntegerField(_('old price'))
    price = models.PositiveIntegerField(_('price'), default=0, blank=True)
    active = models.BooleanField(_('active'), default=True)

    datetime_created = models.DateTimeField(_('DateTime Created'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('DateTime Modified'), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


# Product Comment
class Comment(models.Model):
    PRODUCT_START = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('normal')),
        ('4', _('good')),
        ('5', _('very good')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('product'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                               verbose_name=_('author'))
    body = models.TextField(_('comment'))
    stars = models.CharField(_('stars'), max_length=10, choices=PRODUCT_START)
    active = models.BooleanField(_('active'), default=True)

    datetime_created = models.DateTimeField(_('DateTime Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('DateTime Modified'), auto_now=True)

    def __str__(self):
        return f'{self.author} , {self.body[:30]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
