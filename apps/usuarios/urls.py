from django.urls import path
from apps.usuarios.views import Login, logoutUsuario
from apps.crud.views import ProductListView
from django.contrib.auth.decorators import login_required
from apps.usuarios.views import ListadoUsuario, RegistrarUsuario, EliminarUsuario, UpdateUsuario


urlpatterns = [
    path('',login_required(ProductListView.as_view()), name='crud'),
    path('accounts/login/',Login.as_view(), name ='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('listado_usuarios/', login_required(ListadoUsuario.as_view()), name='listar_usuarios'),
    path('registrar_usuario/', login_required(RegistrarUsuario.as_view()), name='registrar_usuario'),
    path('actualizar_usuario/<int:pk>', login_required(UpdateUsuario.as_view()), name = 'actualizar_usuario'),
    path('eliminar_usuario/<int:pk>', login_required(EliminarUsuario.as_view()), name = 'eliminar_usuario'),
]