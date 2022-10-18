from django.urls import path
from . import views

urlpatterns = [
    path('admin_home',views.admin_home),
    path('approve_sellers',views.approve_sellers),
    path('view_sellers',views.view_sellers),
    path('view_customers',views.view_customers),
    path('change_admin_password',views.change_admin_password)


    

]
