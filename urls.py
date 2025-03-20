from django.urls import path
from .views import home, add_to_cart, cart_view, remove_from_cart

urlpatterns = [
    path('', home, name='home'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('remove-from-cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
]
