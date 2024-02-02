from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from .forms import LoginForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("products:products")
            messages.error(request, 'Invalid login or password.')
    else:
        form = LoginForm()

    context = {
        "form": form
    }
    return render(request, "authentication/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("products:products")
