from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, AdminProductCategory, AdminProduct

from users.models import User
from products.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {'title': 'GeekShop - Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'GeekShop - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'GeekShop - Редактирование пользователя', 'selected_user': selected_user, 'form': form}
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


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
