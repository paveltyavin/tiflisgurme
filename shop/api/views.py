from django.http.response import Http404
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Product, Cart, CartProduct
from . import serializers


class ProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CartView(APIView):
    def get_cart(self):
        try:
            cart_id = self.request.session['cart_id']
        except KeyError:
            return None
        try:
            return Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return None

    def get_product(self):
        try:
            return Product.objects.get(id=self.request.data['product'])
        except Product.DoesNotExist:
            raise Http404

    def get(self, request):
        cart = self.get_cart()
        if cart:
            serializer = serializers.CartSeriazlier(cart)
            return Response(serializer.data)
        else:
            return Response({})

    def post(self, request):
        product = self.get_product()
        cart = self.get_cart()
        if not cart:
            cart = Cart.objects.create()
            self.request.session['cart_id'] = cart.id

        cp, cp_created = CartProduct.objects.get_or_create(cart=cart, product=product)
        cp.quantity += 1
        cp.save()
        cart.cartproduct_set.add(cp)

        serializer = serializers.CartProductSerializer(instance=cp)
        return Response(serializer.data)

    def delete(self, request):
        product = self.get_product()
        cart = self.get_cart()
        if not cart:
            raise Http404

        try:
            cp = CartProduct.objects.get(cart=cart, product=product)
        except CartProduct.DoesNotExist:
            raise Http404

        cp.quantity -= 1
        if cp.quantity <= 0:
            cp.delete()
            return Response({})
        else:
            cp.save()
            serializer = serializers.CartProductSerializer(instance=cp)
            return Response(serializer.data)
