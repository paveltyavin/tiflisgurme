from rest_framework import serializers
from shop.models import Product, Cart, CartProduct


class ProductSerializer(serializers.ModelSerializer):
    thumb = serializers.ReadOnlyField(source='get_thumb')

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'desc',
            'price',
            'thumb',
        )


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = (
            'quantity',
            'product',
        )


class CartSeriazlier(serializers.ModelSerializer):
    cartproduct_set = CartProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = (
            'total_price',
            'total_quantity',
            'cartproduct_set',
        )
