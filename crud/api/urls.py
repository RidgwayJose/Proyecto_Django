from django.urls import path
from crud.api.api import ProductAPIView

urlpatterns = [
    path('producto/', ProductAPIView.as_view(), name = 'producto_api')
]
