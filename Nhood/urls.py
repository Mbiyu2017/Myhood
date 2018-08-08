from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^join/(?P<n_id>\d+)', views.join_nhood, name="join_nhood"),
    url(r'^accounts/profile$', views.userprofile, name="userprofile"),
]
