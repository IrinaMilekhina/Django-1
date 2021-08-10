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


def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        context['products'] = Product.objects.filter(category_id=category_id)
    else:
        context['products'] = Product.objects.all()

    return render(request, 'products/products.html', context)
