from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_cv, name='upload_cv')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)