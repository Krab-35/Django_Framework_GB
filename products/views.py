from django.views.generic import TemplateView
from django.views.generic.list import ListView

from products.models import Product, ProductCategory

from django.conf import settings
from django.core.cache import cache


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


class IndexTemplateView(TemplateView):
    template_name = 'products/index.html'
    extra_context = {'title': 'GeekShop'}


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        self.categories = get_links_menu()
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Пользователи'
        context['categories'] = self.categories
        return context

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        try:
            return qs.filter(category=self.kwargs['pk'])
        except KeyError:
            return qs
