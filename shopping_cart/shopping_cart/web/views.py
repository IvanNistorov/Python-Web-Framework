from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from shopping_cart.accounts.models import ShoppingCartUser
from shopping_cart.web.forms import *
from shopping_cart.web.models import AddProductToUserCart, Products
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


@login_required(login_url='register')
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
    item = AddProductToUserCart.objects.filter(id=product_id).get()
    item.delete()

    return redirect('display cart', username=request.user.username, pk=request.user.pk)


class DeleteProductView(views.DeleteView):
    template_name = 'cart.html'
    model = AddProductToUserCart
    success_url = reverse_lazy('display cart')


class CartDetailsView(views.DetailView):
    model = get_user_model()
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['cart_products'] = AddProductToUserCart.objects.all()

        return context




class UserDeleteView(views.DeleteView):
    template_name = 'delete-profile.html'
    model = get_user_model()
    success_url = reverse_lazy('register')


class UserEditView(views.UpdateView):
    model = get_user_model()
    form_class = ProfileEditForm
    template_name = 'edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'username': self.object.username, 'pk': self.object.pk})


class UserDetailsView(views.DetailView):
    model = get_user_model()
    template_name = 'profile.html'

    def get_name(self):
        if self.object.first_name and self.object.last_name:
            name = self.object.get_full_name
        elif self.object.first_name:
            name = self.object.first_name
        elif self.object.last_name:
            name = self.object.last_name
        else:
            name = ''

        return name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.get_name()

        return context


def success_page(request):
    return render(request, 'success.html')
