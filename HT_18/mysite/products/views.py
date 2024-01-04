from django.shortcuts import render, redirect
from .forms import AddScrapingTaskForm, AddProductForm
from .models import ScrapingTask, Product
from pathlib import Path

import subprocess
import json


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
            create_update_product(product_id)

            existing_tasks = ScrapingTask.objects.filter(name=product_id)
            if not existing_tasks.exists():
                ScrapingTask.objects.create(**form.cleaned_data)

            return redirect("add_product")
    else:
        form = AddScrapingTaskForm()
    return render(request, "products/add_product.html", {"form": form})


def divide_product_id(product_id_arg):
    return product_id_arg.split(", ")


def get_unique_names_from_scraping_task():
    unique_name_list = set()
    model_names = ScrapingTask.objects.values_list('name', flat=True)
    for model_name in model_names:
        name_list = model_name.split(", ")
        unique_name_list.update(name_list)

    return list(unique_name_list)


def create_update_product(product_id):
    path_to_your_script = Path(__file__).resolve().parent / 'scraper.py'

    name_list = product_id.split(", ")
    unique_names = get_unique_names_from_scraping_task()

    for name in name_list:
        command = f'python  {path_to_your_script} {name}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        data_scraper = output.decode("utf-8")
        data_scraper_fixed = json.loads(data_scraper.replace("'", '"'))

        if name in unique_names:
            existing_product = Product.objects.get(product_id=name)

            existing_product.name = data_scraper_fixed["name"]
            existing_product.price = data_scraper_fixed["price"]
            existing_product.brand_name = data_scraper_fixed["brand_name"]
            existing_product.category = data_scraper_fixed["category"]
            existing_product.product_link = data_scraper_fixed["product_link"]

            existing_product.save()
        else:
            Product.objects.create(
                name=data_scraper_fixed["name"],
                price=data_scraper_fixed["price"],
                # short_description=data_scraper_fixed["short_description"],
                brand_name=data_scraper_fixed["brand_name"],
                category=data_scraper_fixed["category"],
                product_link=data_scraper_fixed["product_link"],
                product_id=data_scraper_fixed["product_id"],
            )
