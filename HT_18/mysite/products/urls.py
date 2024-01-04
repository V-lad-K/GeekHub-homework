from django.urls import path
from .views import product
from .views import my_products
from .views import add_product

urlpatterns = [
    path('product/<str:product_id>/', product, name='product'),
    path('add_product/', add_product, name="add_product"),
    path('my_products/', my_products, name='my_products'),
]
