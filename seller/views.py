from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render(request, 'seller/seller_home.html')
    
def addproduct(request):
    return render(request, 'seller/addproduct.html')

def updatestock(request):
    return render(request, 'seller/updatestock.html')

def product_catalog(request):
    return render(request, 'seller/product_catalog.html')

def change_seller_password(request):
    return render(request, 'seller/change_seller_password.html')

