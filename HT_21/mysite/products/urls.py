from django.urls import path

from .views import detail_product
from .views import products
from .views import add_product
from .views import product_category_view
from .views import edit_product_view


app_name = 'products'

urlpatterns = [
    path('add_product/', add_product, name="add_product"),
    path('<str:product_id>/', detail_product, name='detail_product'),
    path('', products, name='products'),
    path('edit/<str:product_id>/', edit_product_view, name='edit_product'),
    path('category/<str:product_category_arg>/',
         product_category_view, name='products_by_category'),
]
