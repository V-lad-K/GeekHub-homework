<<<<<<< HEAD
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

import subprocess
import time
import json


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
                subprocess.Popen(['python', 'save_data.py', product_id])
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
                    defaults_data_str = json.dumps(defaults_data)

                    subprocess.Popen(
                        [
                            'python',
                            'update_data.py',
                            product_id,
                            defaults_data_str,
                            str(category_name)
                        ]
                    )
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
                    subprocess.Popen(['python', 'save_data.py', product_id])
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
=======
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.contrib import messages

from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CheckoutSerializer
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from .serializers import ProductDetailSerializer

from .forms import AddScrapingTaskForm
from .forms import AddToCheckout
from .forms import EditProductForm

from .models import Product
from .models import Category
from .models import ScrapingTask

import subprocess
import time
import json


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
                subprocess.Popen(['python', 'save_data.py', product_id])
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
                    defaults_data_str = json.dumps(defaults_data)

                    subprocess.Popen(
                        [
                            'python',
                            'update_data.py',
                            product_id,
                            defaults_data_str,
                            str(category_name)
                        ]
                    )
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
                    subprocess.Popen(['python', 'save_data.py', product_id])
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


class ProductDetailRetrieveAPIView(RetrieveAPIView):
    """
        API endpoint that allows to show product details
        for postman example: http://127.0.0.1:8000/products/api/product/A119639846/
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'product_id'


class ProductListAPIView(ListAPIView):
    """
        API endpoint that allows to show all products and categories
        for postman example: http://127.0.0.1:8000/products/api/all_products/
    """
    def get(self, request):
        products_instance = Product.objects.values('name', 'price', 'product_id')
        categories_instance = Category.objects.all()

        products_serializer = ProductSerializer(
            instance=products_instance,
            many=True
        )
        categories_serializer = CategorySerializer(
            instance=categories_instance,
            many=True
        )

        for product in products_instance:
            request.session[product["product_id"]] = product
            request.session.modified = True

        return Response({
            "products": products_serializer.data,
            "categories": categories_serializer.data
        })


class ProductByCategoryRetrieveAPIView(RetrieveAPIView):
    """
        API endpoint that allows to show all products by category
        for postman example: http://127.0.0.1:8000/products/api/by_category/2/
    """
    serializer_class = ProductSerializer
    lookup_field = 'category_id'
    queryset = Product.objects.all()

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return self.queryset.filter(category_id=category_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class UpdateDeleteCheckoutAPIView(APIView):
    """
        API endpoint that allows to update or delete a product in checkout
        for postman example for put:
            http://127.0.0.1:8000/products/api/all_products/SPM10387139818/5/
        for postman example for delete:
            http://127.0.0.1:8000/products/api/all_products/SPM10387139818/
    """
    def put(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        quantity = int(kwargs.get("quantity"))

        if not product_id:
            return Response({"error": "Product ID must be provided."})

        try:
            session_product = request.session.get(product_id)
            if not session_product:
                return Response({"error": "Product not found in session."})

            order_list = request.session.get("order", [])
            found_product = next((product for product in order_list
                                  if product["product_id"] == product_id),
                                 None)
            if found_product:
                found_product["quantity"] += quantity
            else:
                session_product["quantity"] = quantity
                order_list.append(session_product)

            request.session["order"] = order_list
            request.session.modified = True

            return Response({"message": "Product added to cart successfully."})
        except KeyError as e:
            return Response({"error": str(e)})

    def delete(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')

        if not product_id:
            return Response({"error": "Product ID must be provided."})

        try:
            order_list = request.session.get("order", [])
            updated_order_list = [product for product in order_list
                                  if product["product_id"] != product_id]
            request.session["order"] = updated_order_list
            request.session.modified = True

            return Response({
                "message": "Product removed from cart successfully."
            })
        except KeyError as e:
            return Response({"error": str(e)})


class CheckoutContentListAPIView(ListAPIView):
    """
        API endpoint that allows to show all products in checkout
        for postman http://127.0.0.1:8000/products/api/checkout/
    """
    def get(self, request):
        checkout_content = request.session["order"]

        checkout_serializer = CheckoutSerializer(
            instance=checkout_content,
            many=True
        )

        return Response({
            "checkout_content": checkout_serializer.data
        })
>>>>>>> 970411dd3de5ed996f005820fcc60d8b4bc41da5
