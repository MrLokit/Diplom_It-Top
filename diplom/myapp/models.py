from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='myapp/img/')

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Связываем заказ с продуктом
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='orders/')  # Сохранение пользовательского фото

    def __str__(self):
        return f'Order by {self.name} for {self.product.name}'
