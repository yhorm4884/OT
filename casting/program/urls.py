
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name= 'program'
urlpatterns = [
    path(_(''), views.dashboard, name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

