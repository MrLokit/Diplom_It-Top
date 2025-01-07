from django.contrib import admin
from .models import Product  # Убедитесь, что оставили только Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')