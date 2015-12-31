from rest_framework.generics import RetrieveAPIView
from shop.models import Product
from . import serializers


class ProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
