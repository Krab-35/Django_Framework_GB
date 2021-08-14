from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'image_address': 'vendor/img/products/Adidas-hoodie.png',
                'price': 6090,
                'added_to_basket': False,
            },
            {
                'name': 'Синяя куртка The North Face',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'image_address': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'price': 23725,
                'added_to_basket': True,
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'image_address': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'price': 3390,
                'added_to_basket': False,
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'description': 'Плотная ткань. Легкий материал.',
                'image_address': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'price': 2340,
                'added_to_basket': False,
            },
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'image_address': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                'price': 13590,
                'added_to_basket': False,
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'image_address': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'price': 2890,
                'added_to_basket': False,
            },
        ]
    }
    return render(request, 'products/products.html', context)
