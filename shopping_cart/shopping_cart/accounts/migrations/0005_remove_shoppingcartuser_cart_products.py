# Generated by Django 4.1.3 on 2022-12-03 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_shoppingcartuser_cart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcartuser',
            name='cart_products',
        ),
    ]
