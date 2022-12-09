from django.urls import path, include

from shopping_cart.web.views import *

urlpatterns = (
    path('<str:username>/edit/<int:pk>/', UserEditView.as_view(), name='edit profile'),
    path('<str:username>/details/<int:pk>/', UserDetailsView.as_view(), name='details profile'),
    path('<str:username>/delete/<int:pk>/', user_delete, name='delete profile'),
    path('<str:username>/cart/<int:pk>/', CartDetailsView.as_view(), name='display cart'),
    path('cart/<int:product_id>/', add_to_cart, name='add items'),
    path('cart/<int:product_id>/', remove_from_cart, name='delete item')
)

