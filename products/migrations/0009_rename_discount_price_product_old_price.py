# Generated by Django 4.0.2 on 2023-09-16 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_discount_price_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_price',
            new_name='old_price',
        ),
    ]