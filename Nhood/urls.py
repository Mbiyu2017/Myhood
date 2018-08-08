from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^join/(?P<n_id>\d+)', views.join_nhood, name="join_nhood"),
    url(r'^accounts/profile$', views.userprofile, name="userprofile"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
