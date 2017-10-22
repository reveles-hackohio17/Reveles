from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^map$', views.map, name='map'),
]
