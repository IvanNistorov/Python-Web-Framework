from django.urls import path, include

from shopping_cart.web.views import *

urlpatterns = (
    path('<str:username>/edit/<int:pk>/', UserEditView.as_view(), name='edit profile'),
    path('<str:username>/details/<int:pk>/', UserDetailsView.as_view(), name='details profile'),
    path('<str:username>/delete/<int:pk>/', UserDeleteView.as_view(), name='delete profile'),
    path('<str:username>/cart/<int:pk>/', CartDetailsView.as_view(), name='display cart'),
    path('cart_remove/<int:product_id>/', remove_from_cart, name='remove item'),
    path('cart/<int:product_id>/', add_to_cart, name='add items'),
    path('success/', success_page, name='success_page')
)

