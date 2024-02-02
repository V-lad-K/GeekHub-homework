from rest_framework import serializers

from .models import Product
from .models import Category


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "product_id"]


class ProductByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CheckoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
