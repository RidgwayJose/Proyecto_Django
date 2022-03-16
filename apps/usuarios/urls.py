from django.urls import path
from apps.usuarios.views import Login, logoutUsuario
from apps.crud.views import ProductListView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(ProductListView.as_view()), name='crud'),
    path('accounts/login/',Login.as_view(), name ='login'),
    path('logout/', login_required(logoutUsuario), name='logout')
]