from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'myapp/home.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def order_form(request, product_id):
    # Получаем продукт по ID
    product = get_object_or_404(Product, id=product_id)

    # Логика обработки заказа, если это необходимо
    if request.method == 'POST':
        # обработать запрашиваемую информацию по форме
        pass

    # Отправляем продукт в шаблон
    return render(request, 'myapp/order_form.html', {'product': product})

def services(request):
    return render(request, 'myapp/services.html')

def services_view(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных
    return render(request, 'myapp/services.html', {'products': products})  # Передаем продукты в шаблон