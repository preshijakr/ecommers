from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request, 'customer/home.html')


def customer_cart(request):
    return render(request, 'customer/cart.html')


def customer_profile(request):
    return render(request, 'customer/profile.html')


def customer_order(request):
    return render(request, 'customer/order.html'),


def customer_order(request):
    return render(request, 'customer/order.html')
    
