from django.shortcuts import render
from json import load


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def load_json():
    with open(r"./products/fixtures/products.json") as out_json:
        return load(out_json)


def products(request):
    context = load_json()
    return render(request, 'products/products.html', context)
