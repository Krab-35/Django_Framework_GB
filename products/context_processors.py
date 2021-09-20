from baskets.models import Basket
from django.template.loader import render_to_string
from django.http import JsonResponse


def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return {'baskets': basket}
