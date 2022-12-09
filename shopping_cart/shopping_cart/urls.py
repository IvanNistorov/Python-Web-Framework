from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('shopping_cart.web.urls')),
    path('', include('shopping_cart.accounts.urls')),
]
