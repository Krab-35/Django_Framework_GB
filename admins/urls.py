from django.urls import path

from admins.views import UserIndexView, UserListView, UserCreateView, UserUpdateView, UserDeleteView,\
    ProductCategoryListView, ProductCategoryCreateView, ProductCategoryUpdateView, \
    ProductCategoryDeleteView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', UserIndexView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),

    path('category/', ProductCategoryListView.as_view(), name='admin_product_category'),
    path('category-create/', ProductCategoryCreateView.as_view(), name='admin_product_category_create'),
    path('category-update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='admin_product_category_update'),
    path('category-delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='admin_product_category_delete'),

    path('product/', ProductListView.as_view(), name='admin_product'),
    path('product-create/', ProductCreateView.as_view(), name='admin_product_create'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_product_update'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_product_delete'),
]
