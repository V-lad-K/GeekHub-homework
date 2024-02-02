<<<<<<< HEAD
from django.urls import path
from .views import checkout


app_name = 'checkout'

urlpatterns = [
    # path("checkout/", checkout, name="checkout"),
    path("", checkout, name="checkout"),
]
=======
from django.urls import path
from .views import checkout


app_name = 'checkout'

urlpatterns = [
    # path("checkout/", checkout, name="checkout"),
    path("", checkout, name="checkout"),
]
>>>>>>> 970411dd3de5ed996f005820fcc60d8b4bc41da5
