from django.urls import path
from apps.crud.api.views.general_views import ProductListAPiView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('prod/', login_required(ProductListAPiView.as_view()), name = 'productAPI_list_view')
    #path('producto/', ProductAPIView.as_view(), name = 'producto_api')
]
