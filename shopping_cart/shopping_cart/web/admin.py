from django.contrib import admin

from shopping_cart.web.models import Products


@admin.register(Products)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
