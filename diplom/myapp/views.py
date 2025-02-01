from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Product

def home(request):
    return render(request, 'myapp/home.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def order_form(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        pass

    return render(request, 'myapp/order_form.html', {'product': product})

def services(request):
    return render(request, 'myapp/services.html')

def services_view(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'myapp/services.html', {'products': products})



def order_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        comments = request.POST.get('comments')
        photo = request.FILES.get('photo')

        Order.objects.create(
            product=product,
            name=name,
            contact=contact,
            comments=comments,
            photo=photo
        )

        return redirect('success_view')

    return render(request, 'myapp/order_form.html', {'product': product})


def success_view(request):
    return render(request, 'myapp/success.html')