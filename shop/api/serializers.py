from rest_framework import serializers
from sorl.thumbnail.shortcuts import get_thumbnail
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField()

    def get_thumb(self, obj):
        if obj.image is None:
            return None
        try:
            t = get_thumbnail(obj.image, 'x250')
        except IOError:
            return None
        if t:
            return t.url
        else:
            return None

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'desc',
            'price',
            'thumb',
        )
