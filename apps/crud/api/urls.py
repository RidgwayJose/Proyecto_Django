from django.urls import path
from apps.crud.api.views.general_views import ProductListAPiView

urlpatterns = [
    path('prod/', ProductListAPiView.as_view(), name = 'productAPI_list_view')
    #path('producto/', ProductAPIView.as_view(), name = 'producto_api')
]
