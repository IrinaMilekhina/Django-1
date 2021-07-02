from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.
# модели = таблицы в БД


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True,
                                   null=True)  # если не стоит null, то поле по прежнему обязательно к заполнению, но будет заполняться пустой строкой


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images',
                              blank=True)  # папка products_images создается автоматически после миграций
    description = models.TextField(blank=True, null=True)
    price = MoneyField(decimal_places=2, default=0, default_currency='RUB',
                       max_digits=11)  # библиотека https://github.com/django-money/django-money
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # on_delete=models.CASCADE/SET_NULL/PROTECT
