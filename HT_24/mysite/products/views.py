from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.contrib import messages

from .forms import AddScrapingTaskForm
from .forms import AddToCheckout
from .forms import EditProductForm

from .models import Product
from .models import Category
from .models import ScrapingTask

from .tasks.task_save_data import save_task
from .tasks.task_save_data import save_product_and_category
from .tasks.task_update_data import update_product

import time


def detail_product(request, product_id):
    product_context = get_object_or_404(Product, product_id=product_id)
    user = request.user
    context = {
        "product": product_context,
        "user": user
    }
    return render(request, "products/product.html", context)


def products(request):
    user = request.user
    if request.method == "POST":
        form = AddToCheckout(request.POST)
        if form.is_valid():
            if user.is_authenticated:
                quantity = form.cleaned_data.get("quantity")
                product_id = form.cleaned_data.get("product_id")
                session_product = request.session[product_id]
                order_list = request.session.get("order") or []

                found_product = next(
                    (product for product in order_list
                        if session_product["name"] == product["name"]),
                    None)

                if found_product:
                    found_product["quantity"] += quantity
                else:
                    order_list.append({**session_product, "quantity": quantity})

                request.session["order"] = order_list
                request.session.modified = True
            else:
                messages.error(
                    request,
                    'You are not allowed to add the product to the cart'
                )

    my_products = Product.objects.values('name', 'price', "product_id")
    categories = Category.objects.all()

    for product in my_products:
        request.session[product["product_id"]] = product
        request.session.modified = True

    context = {
        "products": my_products,
        "categories": categories,
        "user": user
    }
    return render(request, "products/my_products.html", context)


def add_product(request):
    user = request.user
    if user.is_superuser:
        if request.method == "POST":
            form = AddScrapingTaskForm(request.POST)
            if form.is_valid():
                product_id = form.cleaned_data.get("name")
                save_product_and_category.delay(product_id)
                save_task.delay(product_id)
                return redirect("products:add_product")
        else:
            form = AddScrapingTaskForm()
        return render(request, "products/add_product.html", {"form": form})
    else:
        return redirect("products:products")


def product_category_view(request, product_category_arg):
    user = request.user
    if request.method == "POST":
        form = AddToCheckout(request.POST)
        if form.is_valid():
            if user.is_authenticated:
                quantity = form.cleaned_data.get("quantity")
                product_id = form.cleaned_data.get("product_id")
                session_product = request.session[product_id]
                order_list = request.session.get("order") or []

                found_product = next(
                    (product for product in order_list
                     if session_product["name"] == product["name"]),
                    None)

                if found_product:
                    found_product["quantity"] += quantity
                else:
                    order_list.append({**session_product, "quantity": quantity})

                request.session["order"] = order_list
                request.session.modified = True
            else:
                messages.error(
                    request,
                    'You are not allowed to add the product to the cart'
                )
            return redirect(
                'products:products_by_category',
                product_category_arg=product_category_arg
            )
    category = get_object_or_404(Category, name=product_category_arg)
    products_by_category = category.products.all()
    context = {
        "products": products_by_category,
        "category": category
    }

    return render(request, "products/product_by_category.html", context)


def edit_product_view(request, product_id):
    user = request.user
    if not user.is_superuser or not user.is_authenticated:
        messages.error(request, 'You are not superuser or not registered')
        return redirect("products:products")
    product = get_object_or_404(Product, product_id=product_id)
    scraping_task = get_object_or_404(ScrapingTask, name=product_id)

    if request.method == "POST":
        form = EditProductForm(request.POST)
        if form.is_valid():
            command = form.cleaned_data.get("command")
            match command:
                case "EditProduct":
                    category_name = form.cleaned_data.get("category_id")
                    defaults_data = {
                        'name': form.cleaned_data.get("name"),
                        'price': form.cleaned_data.get("price"),
                        "short_description": form.cleaned_data.get("short_description"),
                        "brand_name": form.cleaned_data.get("brand_name"),
                        "product_link": form.cleaned_data.get("product_link"),
                    }
                    update_product.delay(defaults_data, product_id, str(category_name))
                    time.sleep(2)
                    return redirect(
                        'products:edit_product',
                        product_id=product_id
                    )
                case "DeleteProduct":
                    product.delete()
                    scraping_task.delete()

                    return redirect('products:products')
                case "ScrapingUpdate":
                    save_product_and_category.delay(product_id)
                    save_task.delay(product_id)
                    time.sleep(2)
                    return redirect(
                        'products:edit_product',
                        product_id=product_id
                    )
    else:
        form = EditProductForm(
            initial={
                "name": product.name,
                "price": product.price,
                "short_description": product.short_description,
                "brand_name": product.brand_name,
                "product_link": product.product_link,
                "category_id": product.category_id,
                "product_id": product.product_id
            })

    context = {
        "product": product,
        "form": form
    }
    return render(request, "products/edit_product.html", context)
