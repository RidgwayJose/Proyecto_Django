from django.urls import path
from crud.api.api import product_api_view #, ProductAPIView

urlpatterns = [
    path('producto/', product_api_view, name = 'producto_api')
    #path('producto/', ProductAPIView.as_view(), name = 'producto_api')
]
