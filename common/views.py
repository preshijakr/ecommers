from django.shortcuts import render

# Create your views here.
def project_home(request):
    return render(request,'common/project_home.html')


def reseller_signup(request):
    return render(request,'common/reseller_signup.html')

    
def reseller_login(request):
    return render(request,'common/reseller_login.html')

def customer_signup(request):
    return render(request,'common/customer_signup.html')

def customer_login(request):
    return render(request,'common/customer_login.html')

