from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import AddScrapingTaskForm
from .forms import AddToCheckout
from .models import Product

import subprocess


def detail_product(request, product_id):
    product_context = get_object_or_404(Product, product_id=product_id)
    context = {
        "product": product_context
    }
    return render(request, "products/product.html", context)


def products(request):
    if request.method == "POST":
        form = AddToCheckout(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get("quantity")
            product_id = form.cleaned_data.get("product_id")
            session_product = request.session[product_id]
            order_list = request.session.get("order") or []

            found_product = next((product for product in order_list
                                  if session_product["name"] == product["name"]),
                                 None)

            if found_product:
                found_product["quantity"] += quantity
            else:
                order_list.append({**session_product, "quantity": quantity})

            request.session["order"] = order_list
            request.session.modified = True

    my_products = Product.objects.values('name', 'price', "product_id")

    for product in my_products:
        request.session[product["product_id"]] = product
        request.session.modified = True

    context = {
        "products": my_products
    }
    return render(request, "products/my_products.html", context)


def add_product(request):
    if request.method == "POST":
        form = AddScrapingTaskForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data.get("name")
            name_list = product_id.split(", ")

            for name in name_list:
                subprocess.Popen(['python', 'scraper.py', name])

            return redirect("add_product")
    else:
        form = AddScrapingTaskForm()
    return render(request, "products/add_product.html", {"form": form})
