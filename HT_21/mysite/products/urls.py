<<<<<<< HEAD
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
=======
from django.urls import path

from .views import detail_product
from .views import ProductListAPIView
from .views import ProductByCategoryRetrieveAPIView
from .views import CheckoutContentListAPIView
from .views import UpdateDeleteCheckoutAPIView
from .views import products
from .views import add_product
from .views import product_category_view
from .views import edit_product_view
from .views import ProductDetailRetrieveAPIView


app_name = 'products'

urlpatterns = [
    path('add_product/', add_product, name="add_product"),
    path('<str:product_id>/', detail_product, name='detail_product'),
    path('', products, name='products'),
    path('edit/<str:product_id>/', edit_product_view, name='edit_product'),
    path('category/<str:product_category_arg>/',
         product_category_view, name='products_by_category'),

    path("api/product/<str:product_id>/",
         ProductDetailRetrieveAPIView.as_view(), name="api_detail_products"),
    path("api/all_products/",
         ProductListAPIView.as_view(), name="all_products"),
    path("api/all_products/<str:product_id>/",
         UpdateDeleteCheckoutAPIView.as_view(), name="delete_product"),
    path("api/all_products/<str:product_id>/<str:quantity>/",
         UpdateDeleteCheckoutAPIView.as_view(),
         name="from_products_to_checkout"),
    path("api/by_category/<str:category_id>/",
         ProductByCategoryRetrieveAPIView.as_view(), name="by_category"),
    path("api/checkout/",
         CheckoutContentListAPIView.as_view(), name="checkout_content")
]
>>>>>>> 970411dd3de5ed996f005820fcc60d8b4bc41da5
