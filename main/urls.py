from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from . import views as main_views
from django.conf.urls.static import static

urlpatterns = [
    path('', main_views.home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)