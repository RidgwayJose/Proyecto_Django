from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.crud.views import ProductListView , ProductUpdateView, ProductCreateView, ProductDeleteView #edit_product 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar/', login_required(ProductListView.as_view()), name='listProduct'),
    path('crear', login_required(ProductCreateView.as_view()), name = 'createProduct'),
    path('editar/<int:pk>', login_required(ProductUpdateView.as_view()), name = 'editProduct'),
    path('eliminar/<int:pk>', login_required(ProductDeleteView.as_view()), name = 'deleteProduct'),
    #path('editar/<int:id>', edit_product),
    #path('eliminacionProducto/<int:id>', ModelDeleteView.as_view(), name='classDelete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)