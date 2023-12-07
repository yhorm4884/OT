from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'competitor'

urlpatterns = [
    path('', views.show_competitors, name='competitor'),
    path('<slug:competitor_slug>', views.competitor_detail, name='competitor_detail'),
]
