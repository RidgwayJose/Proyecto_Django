#Convertir a Json
from rest_framework import serializers
from crud.models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    exclude = ('status',)
    