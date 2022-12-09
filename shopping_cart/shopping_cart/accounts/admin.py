from django.contrib import admin

from shopping_cart.accounts.models import ShoppingCartUser


@admin.register(ShoppingCartUser)
class AuthorAdmin(admin.ModelAdmin):
    pass
