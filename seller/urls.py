from django.urls import path
from . import views

urlpatterns = [
    path('seller_home',views.seller_home),
    path('addproduct',views.addproduct),
    path('update',views.updatestock),
    path('product_catalog',views.product_catalog),
    path('seller_password',views.change_seller_password)
]
