from django.urls import path

from .views import ProductListAPIView
from .views import ProductByCategoryRetrieveAPIView
from .views import CheckoutContentListAPIView
from .views import UpdateDeleteCheckoutAPIView
from .views import ProductDetailRetrieveAPIView
from .views import DeleteAllProductsAPIView

app_name = 'api'

urlpatterns = [
    path("product/<str:product_id>/",
         ProductDetailRetrieveAPIView.as_view(), name="api_detail_products"),
    path("all_products/",
         ProductListAPIView.as_view(), name="api_all_products"),
    path("all_products/by_category/<str:category_id>/",
         ProductByCategoryRetrieveAPIView.as_view(),
         name="api_product_by_category"),
    path("all_products/<str:product_id>/",
         UpdateDeleteCheckoutAPIView.as_view(),
         name="api_delete_product_in_checkout_from_products"),
    path("all_products/<str:product_id>/<str:quantity>/",
         UpdateDeleteCheckoutAPIView.as_view(),
         name="api_add_product_in_checkout_from_products"),
    path("checkout/",
         CheckoutContentListAPIView.as_view(), name="api_checkout_content"),
    path("checkout/delete_all/",
         DeleteAllProductsAPIView.as_view(), name="api_checkout_delete_all"),
    path("checkout/<str:product_id>/",
         UpdateDeleteCheckoutAPIView.as_view(),
         name="api_delete_product_in_checkout_from_checkout"),
    path("checkout/<str:product_id>/<str:quantity>/",
         UpdateDeleteCheckoutAPIView.as_view(),
         name="api_add_product_in_checkout_from_checkout"),
]
