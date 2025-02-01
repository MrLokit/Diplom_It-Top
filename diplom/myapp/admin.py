from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'is_active')
    list_editable = ('is_active',)
    fields = ('name', 'price', 'image', 'is_active', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'contact', 'comments', 'photo')
