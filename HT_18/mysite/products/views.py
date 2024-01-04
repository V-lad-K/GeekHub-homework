from django.shortcuts import redirect
from django.shortcuts import render
from .forms import AddScrapingTaskForm
from .models import Product

import subprocess


def product(request, product_id):
    product_context = Product.objects.get(product_id=product_id)
    context = {
        "product": product_context
    }
    return render(request, "products/product.html", context)


def my_products(request):
    products = Product.objects.values('name', 'price', "product_id")
    context = {
        "products": products
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
