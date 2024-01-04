from django.contrib import admin
from .models import Product, ScrapingTask
# Register your models here.


admin.site.register(ScrapingTask)
admin.site.register(Product)