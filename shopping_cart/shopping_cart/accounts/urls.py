from django.urls import path

from shopping_cart.accounts.views import *
from shopping_cart.web.views import index

urlpatterns = (
    path('', index, name='home page'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

)
