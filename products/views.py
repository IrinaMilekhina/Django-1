from django.shortcuts import render
from datetime import date
import json

from products.models import Product, ProductCategory

# Create your views here.
# функции = контроллеры = вьюхи

def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
