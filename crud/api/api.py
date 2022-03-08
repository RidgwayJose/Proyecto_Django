from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from crud.models import Product
from crud.api.serializers import ProductSerializer

'''
class ProductAPIView(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many = True) #many por ser listado de datos
        return Response(product_serializer.data) #.data = POST
'''

@api_view(['GET', 'POST'])
def product_api_view(request):
    
    if request.method == 'GET':
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many = True) #many por serlistado de datos
        return Response(product_serializer.data)
    
    elif request.method ==  'POST':
         product_serializer = ProductSerializer(data = request.data)
         if product_serializer.is_valid():
             product_serializer.save()
             return Response(product_serializer.data)
         return Response(product_serializer.errors)