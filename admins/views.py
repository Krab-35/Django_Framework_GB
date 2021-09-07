from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
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


# @user_passes_test(lambda u: u.is_staff)
# def admin_product_category_delete(request, id):
#     selected_category = ProductCategory.objects.get(id=id)
#     selected_category.delete()
#     return HttpResponseRedirect(reverse('admins:admin_product_category'))


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-product-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_product_category')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCategoryDeleteView, self).dispatch(request, *args, **kwargs)


# PRODUCTS
@user_passes_test(lambda u: u.is_staff)
def admin_product(request):
    context = {
        'title': 'GeekShop - Товаров',
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-product.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_update(request, id):
    selected_product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = AdminProduct(instance=selected_product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))
    else:
        form = AdminProduct(instance=selected_product)
    context = {
        'title': 'GeekShop - Редактирование товара',
        'selected_product': selected_product,
        'form': form,
    }
    return render(request, 'admins/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_create(request):
    if request.method == 'POST':
        form = AdminProduct(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))
    else:
        form = AdminProduct()
    context = {'title': 'GeekShop - Создание категории', 'form': form}
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_delete(request, id):
    selected_product = Product.objects.get(id=id)
    selected_product.delete()
    return HttpResponseRedirect(reverse('admins:admin_product'))
