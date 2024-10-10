from django.contrib import admin

from goods.models import Category, Products


admin.site.register(Category)
admin.site.register(Products)