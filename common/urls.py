from django.urls import path
from . import views

urlpatterns = [
    path('home', views.project_home, name='home'),
    path('signup', views.reseller_signup, name='signup'),
    path('login', views.reseller_login, name='login'),
    path('cust_signup', views.customer_signup, name='cust_signup'),
    path('cust_login', views.customer_login, name='cust_login')

]
