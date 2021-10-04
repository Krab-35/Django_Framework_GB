from django.contrib import admin

from products.models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'is_active')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category', 'is_active')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('-name',)
    search_fields = ('name',)
