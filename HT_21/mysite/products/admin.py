<<<<<<< HEAD
from django.contrib import admin

from .models import Product
from .models import ScrapingTask
from .models import Category


admin.site.register(ScrapingTask)
admin.site.register(Product)
admin.site.register(Category)
=======
from django.contrib import admin
from .models import Product, ScrapingTask, Category
# Register your models here.


admin.site.register(ScrapingTask)
admin.site.register(Product)
admin.site.register(Category)
>>>>>>> 970411dd3de5ed996f005820fcc60d8b4bc41da5
