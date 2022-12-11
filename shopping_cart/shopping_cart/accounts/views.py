from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import generic as view
from django.contrib.auth import views as auth_views

from shopping_cart.accounts.forms import *
from shopping_cart.accounts.models import ShoppingCartUser
from django.contrib import admin


class UserRegisterView(view.CreateView):
    model = ShoppingCartUser
    form_class = ShoppingCartUserCreateForm
    template_name = 'register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = ShoppingCartUserLoginForm
    template_name = 'login-page.html'
    next_page = reverse_lazy('home page')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')

