from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from crud.views import HomeListView

urlpatterns = [
    path('', HomeListView.as_view(), name='classHome'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)