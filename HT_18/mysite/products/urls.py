from django.urls import path
from .views import detail_product
from .views import products
from .views import add_product


app_name = 'products'

urlpatterns = [
    path('products/<str:product_id>/', detail_product, name='detail_product'),
    path('add_product/', add_product, name="add_product"),
    path('products/', products, name='products'),
]
