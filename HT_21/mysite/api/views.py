from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CheckoutSerializer
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from .serializers import ProductDetailSerializer

from products.models import Product
from products.models import Category


class ProductDetailRetrieveAPIView(RetrieveAPIView):
    """
        API class that allows you to show product details
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'product_id'


class ProductListAPIView(ListAPIView):
    """
        API class that allows you to show all products and categories
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
        API class that allows you to show all products by category
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
        API class that allows you to update or delete
        a product in the checkout
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
            if quantity < 0 and found_product["quantity"] + quantity < 0:
                return Response({"error message": "Quantity of products is negative."})
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
        API class that allows you to show all products in checkout
    """
    def get(self, request):
        try:
            checkout_content = request.session["order"]

            checkout_serializer = CheckoutSerializer(
                instance=checkout_content,
                many=True
            )

            return Response({
                "checkout_content": checkout_serializer.data
            })
        except KeyError:
            return Response({
                "order": "order is empty"
            })
