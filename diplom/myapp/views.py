from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def order_form(request):
    return render(request, 'myapp/order_form.html')

def services(request):
    return render(request, 'myapp/services.html')
