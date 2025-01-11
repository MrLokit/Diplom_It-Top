from django.contrib import admin
from .models import Product, Order  # Убедитесь, что обе модели импортированы

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'contact', 'comments', 'photo')  # Теперь используем правильные поля
