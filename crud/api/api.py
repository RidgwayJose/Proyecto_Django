from rest_framework.response import Response
from rest_framework.views import APIView
from crud.models import Product
from crud.api.serializers import ProductSerializer

class ProductAPIView(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many = True) #many por ser listado de datos
        return Response(product_serializer.data)