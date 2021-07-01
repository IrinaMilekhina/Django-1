from django.shortcuts import render
from datetime import date
import json

# Create your views here.
# функции = контроллеры = вьюхи

with open('products/fixtures/products.json', encoding='utf-8') as f:
    import_products = json.load(f)

def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'date': date.today(),
        'products': import_products,
    }
    return render(request, 'products/products.html', context)
