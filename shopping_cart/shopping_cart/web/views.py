from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from shopping_cart.accounts.models import ShoppingCartUser
from shopping_cart.web.forms import *
from shopping_cart.web.models import Products, AddProductToUserCart
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


def get_profile():
    profile = ShoppingCartUser.objects.all()
    if not profile.is_superuser or not profile.is_staff or profile is None:
        return redirect('register')
    return profile


def index(request):
    product = Products.objects.all()

    context = {
        'products': product,
    }

    return render(request, 'index.html', context)


def add_to_cart(request, product_id):
    AddProductToUserCart.objects.create(product_id=product_id, user=request.user)

    return redirect('home page')


def remove_from_cart(request, product_id):

    product = AddProductToUserCart.pk
    product.__delete__(AddProductToUserCart.pk)

    return redirect('display cart')


class CartDetailsView(views.DetailView):
    model = get_user_model()
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['cart_products'] = AddProductToUserCart.objects.all()

        return context


def user_delete(request, username, pk):
    return render(request, 'delete-profile.html')


class UserEditView(views.UpdateView):
    model = get_user_model()
    form_class = ProfileEditForm
    template_name = 'edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'username': self.object.username, 'pk': self.object.pk})


class UserDetailsView(views.DetailView):
    model = get_user_model()
    template_name = 'profile.html'
