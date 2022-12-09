from django import forms

from shopping_cart.accounts.models import ShoppingCartUser
from shopping_cart.web.models import Products


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Profile Picture',
            'gender': 'Gender',
        }

