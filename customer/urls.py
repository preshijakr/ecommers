from django.urls import path
from . import views

app_name='customer'
urlpatterns = [
    path('customer_home',views.customer_home,name='customer_home'),
    path('cart',views.cart, name='customer_cart'),
    path('password',views.change_password),
    path('myorders',views.myorders),
    path('details',views.product_details)
    

]
