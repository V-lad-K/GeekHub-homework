from django.urls import path
from .views import login_view
from .views import logout_view


app_name = 'authentication'

urlpatterns = [
    path('', login_view, name="login"),
    path("logout/", logout_view, name="logout")
]
