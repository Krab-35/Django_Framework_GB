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
    extra_context = {'title': 'GeekShop - Admin'}

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


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

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


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
        return super(UserListView, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.is_staff)
def admin_product_category(request):
    context = {
        'title': 'GeekShop - Категории товаров',
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'admins/admin-product-category.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_category_update(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = AdminProductCategory(instance=selected_category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product_category'))
    else:
        form = AdminProductCategory(instance=selected_category)
    context = {
        'title': 'GeekShop - Редактирование категории',
        'selected_category': selected_category,
        'form': form,
    }
    return render(request, 'admins/admin-product-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_category_create(request):
    if request.method == 'POST':
        form = AdminProductCategory(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product_category'))
    else:
        form = AdminProductCategory()
    context = {'title': 'GeekShop - Создание категории', 'form': form}
    return render(request, 'admins/admin-product-category-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_product_category_delete(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    selected_category.delete()
    return HttpResponseRedirect(reverse('admins:admin_product_category'))


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
