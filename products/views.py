from django.shortcuts import render
from os import path
from json import load


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def load_json():
    try:
        with open(path.join(path.dirname(__file__), 'fixtures/products.json'), encoding='utf-8') as out_json:
            return load(out_json)
    except IOError:
        return []


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': load_json(),
    }
    return render(request, 'products/products.html', context)
