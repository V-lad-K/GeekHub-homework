from django.contrib import admin
from .models import Product, ScrapingTask, Category
# Register your models here.


admin.site.register(ScrapingTask)
admin.site.register(Product)
admin.site.register(Category)
