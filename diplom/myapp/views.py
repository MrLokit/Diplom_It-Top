from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Product

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



def order_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Получаем продукт по ID

    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        comments = request.POST.get('comments')
        photo = request.FILES.get('photo')  # Получаем загруженный файл

        # Создаем новый заказ, связывая его с продуктом
        Order.objects.create(
            product=product,
            name=name,
            contact=contact,
            comments=comments,
            photo=photo  # Сохраняем файл в поле модели
        )

        return redirect('success_view')  # Перенаправляем на страницу успеха

    # Отправляем на страницу оформления заказа с продуктом
    return render(request, 'myapp/order_form.html', {'product': product})


def success_view(request):
    return render(request, 'myapp/success.html')