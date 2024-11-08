# Generated by Django 5.1.1 on 2024-10-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cart_products'),
        ('shop', '0009_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='cart.CartItem', to='shop.product'),
        ),
    ]