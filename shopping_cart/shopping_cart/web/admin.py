from django.contrib import admin

from shopping_cart.web.models import *


@admin.register(Products)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AddProductToUserCart)
class AuthorAdmin(admin.ModelAdmin):
    pass
