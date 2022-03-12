from rest_framework import generics
from apps.crud.models import Product
from apps.crud.api.serializers import ProductSerializer

class ProductListAPiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(status = True)

