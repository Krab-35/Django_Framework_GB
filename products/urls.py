from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('', cache_page(30)(ProductListView.as_view()), name='product'),
    path('<int:pk>/', ProductListView.as_view(), name='category'),
]
