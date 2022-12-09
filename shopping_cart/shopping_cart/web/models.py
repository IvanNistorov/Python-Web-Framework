from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Products(models.Model):
    PRODUCT_NAME_MAX_LENGTH = 20
    PRODUCT_TYPE_MAX_LENGTH = 30
    PRODUCT_DETAILS_MAX_LENGTH = 200

    name = models.CharField(max_length=PRODUCT_NAME_MAX_LENGTH)
    image = models.URLField()
    price = models.FloatField()
    product_type = models.CharField(max_length=PRODUCT_TYPE_MAX_LENGTH)
    details = models.CharField(max_length=PRODUCT_DETAILS_MAX_LENGTH)


class AddProductToUserCart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.RESTRICT)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
