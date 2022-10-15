from django.urls import path
from . import views

urlpatterns = [
    path('s_home',views.seller_home)
]
