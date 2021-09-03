from django.urls import path

from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_user_delete,\
    admin_product_category, admin_product_category_create, admin_product_category_update

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:id>/', admin_user_delete, name='admin_user_delete'),

    path('category/', admin_product_category, name='admin_product_category'),
    path('category-create/', admin_product_category_create, name='admin_product_category_create'),
    path('category-update/<int:id>/', admin_product_category_update, name='admin_product_category_update'),
]
