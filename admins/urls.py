from django.urls import path

from admins.views import UserIndexView, UserListView, UserCreateView, UserUpdateView, UserDeleteView,\
    admin_product_category, admin_product_category_create, admin_product_category_update, \
    admin_product_category_delete, admin_product, admin_product_create, admin_product_update, admin_product_delete

app_name = 'admins'

urlpatterns = [
    path('', UserIndexView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),

    path('category/', admin_product_category, name='admin_product_category'),
    path('category-create/', admin_product_category_create, name='admin_product_category_create'),
    path('category-update/<int:id>/', admin_product_category_update, name='admin_product_category_update'),
    path('category-delete/<int:id>/', admin_product_category_delete, name='admin_product_category_delete'),

    path('product/', admin_product, name='admin_product'),
    path('product-create/', admin_product_create, name='admin_product_create'),
    path('product-update/<int:id>/', admin_product_update, name='admin_product_update'),
    path('product-delete/<int:id>/', admin_product_delete, name='admin_product_delete'),
]
