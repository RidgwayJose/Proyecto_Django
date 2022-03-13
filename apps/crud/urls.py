from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.crud.views import ProductListView , ProductUpdateView, ProductCreateView, ProductDeleteView #,edit_product 

urlpatterns = [
    path('listar/', ProductListView.as_view(), name='listProduct'),
    path('crear', ProductCreateView.as_view(), name = 'createProduct'),
    path('editar/<int:pk>', ProductUpdateView.as_view(), name = 'editProduct'),
    path('eliminar/<int:pk>', ProductDeleteView.as_view(), name = 'deleteProduct'),
    #path('editar/<int:id>', edit_product),
    #path('eliminacionProducto/<int:id>', ModelDeleteView.as_view(), name='classDelete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)