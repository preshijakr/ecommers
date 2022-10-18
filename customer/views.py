from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request, 'customer/customer_home.html')
    
def cart(request):
    return render(request, 'customer/cart.html')
    
def change_password(request):
    return render(request, 'customer/change_password.html')
    
def myorders(request):
    return render(request, 'customer/myorders.html')
    
def product_details(request):
    return render(request, 'customer/product_details.html')




    
