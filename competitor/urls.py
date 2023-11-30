# En urls.py

from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'competitor'

urlpatterns = [
    path(_('competitors'), views.show_competitors, name='all_competitors'),
]
