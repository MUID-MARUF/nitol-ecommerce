from django.contrib import admin
from .models import Product, Category

#Product model registration
admin.site.register(Product)

#Category model registration
admin.site.register(Category)

