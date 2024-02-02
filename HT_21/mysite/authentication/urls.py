<<<<<<< HEAD
from django.urls import path
from .views import login_view
from .views import logout_view


app_name = 'authentication'

urlpatterns = [
    path('', login_view, name="login"),
    path("logout/", logout_view, name="logout")
]
=======
from django.urls import path
from .views import login_view
from .views import logout_view


app_name = 'authentication'

urlpatterns = [
    path('', login_view, name="login"),
    path("logout/", logout_view, name="logout")
]
>>>>>>> 970411dd3de5ed996f005820fcc60d8b4bc41da5
