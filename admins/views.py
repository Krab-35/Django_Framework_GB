from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from django.utils.decorators import method_decorator

from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, AdminProductCategory, AdminProduct

from users.models import User
from products.models import Product, ProductCategory


class UserIndexView(TemplateView):
    template_name = 'admins/index.html'
    extra_context = {'title': 'GeekShop - Админ'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(TemplateView, self).dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:admin_users')
    extra_context = {'title': 'GeekShop - Админ | Создание пользователя'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    extra_context = {'title': 'GeekShop - Админ | Редактирование пользователя'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-product-category.html'
    extra_context = {'title': 'GeekShop - Админ | Категории товаров'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryListView, self).dispatch(request, *args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-product-category-create.html'
    form_class = AdminProductCategory
    success_url = reverse_lazy('admins:admin_product_category')
    extra_context = {'title': 'GeekShop - Админ | Создание категории'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryCreateView, self).dispatch(request, *args, **kwargs)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'admins/admin-product-category-update-delete.html'
    form_class = AdminProductCategory
    success_url = reverse_lazy('admins:admin_product_category')
    extra_context = {'title': 'GeekShop - Админ | Редактирование категории'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryUpdateView, self).dispatch(request, *args, **kwargs)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-product-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_product_category')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryDeleteView, self).dispatch(request, *args, **kwargs)


# PRODUCTS
class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-product.html'
    extra_context = {'title': 'GeekShop - Админ | Товары'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = AdminProduct
    success_url = reverse_lazy('admins:admin_product')
    extra_context = {'title': 'GeekShop - Админ | Товары'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = AdminProduct
    success_url = reverse_lazy('admins:admin_product')
    extra_context = {'title': 'GeekShop - Админ | Редактирование товара'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    success_url = reverse_lazy('admins:admin_product')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)
