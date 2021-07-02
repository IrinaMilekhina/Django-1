from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.
# модели = таблицы в БД


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    # если не стоит null, то поле по прежнему обязательно к заполнению, но будет заполняться пустой строкой
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    # папка products_images создается автоматически после миграций
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True, null=True)
    # библиотека https://github.com/django-money/django-money
    price = MoneyField(decimal_places=2, default=0, default_currency='RUB', max_digits=11)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # on_delete=models.CASCADE/SET_NULL/PROTECT

    def __str__(self):
        return f'{self.name} | {self.category.name}'
