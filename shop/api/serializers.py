from rest_framework import serializers
from shop.models import Product


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
