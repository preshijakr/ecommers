from django.urls import path
from . import views

urlpatterns = [
    path('home',views.customer_home),
    path('cart',views.customer_cart),
    path('profile',views.customer_profile),
    path('order',views.customer_order)
]
