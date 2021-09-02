from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',)
    inlines = (BasketAdmin,)
    search_fields = ('username', 'first_name', 'last_name',)
