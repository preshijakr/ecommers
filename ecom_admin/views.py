from django.shortcuts import render

# Create your views here.
def admin_home(request):
    return render(request, 'ecom_admin/admin_home.html')

def approve_sellers(request):
    return render(request, 'ecom_admin/approve_sellers.html')

def view_sellers(request):
    return render(request, 'ecom_admin/view_sellers.html')

def view_customers(request):
    return render(request, 'ecom_admin/view_customers.html')

def change_admin_password(request):
    return render(request, 'ecom_admin/change_admin_password.html')