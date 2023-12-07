# program/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from . import views

app_name= 'program'
urlpatterns = [
    path('', views.dashboard, name='home'),
    path('search/', views.global_search, name='global_search'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
