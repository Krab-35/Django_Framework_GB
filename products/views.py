from django.views.generic import TemplateView
from django.views.generic.list import ListView

from products.models import Product, ProductCategory


class IndexTemplateView(TemplateView):
    template_name = 'products/index.html'
    extra_context = {'title': 'GeekShop'}


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        self.categories = ProductCategory.objects.all()
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
