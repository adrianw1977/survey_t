from django.conf.urls import url
from . import views
# Models -- views -- TEMPLATES

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show),
    url(r'^new_user$', views.create)
]