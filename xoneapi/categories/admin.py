from django.contrib import admin

from categories.models import Category, BasicCategory, UserCategory


admin.site.register(Category)
admin.site.register(BasicCategory)
admin.site.register(UserCategory)

