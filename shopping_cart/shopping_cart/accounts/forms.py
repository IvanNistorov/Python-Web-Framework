from django.contrib.auth.forms import *

from shopping_cart.accounts.models import ShoppingCartUser


class ShoppingCartUserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = 'Repeat Password'

    class Meta(UserCreationForm.Meta):
        model = ShoppingCartUser
        fields = ('username', 'email')


class ShoppingCartUserLoginForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = ShoppingCartUser
        fields = ('username', 'password')

