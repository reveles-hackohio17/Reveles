from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_map, name='main_map'),
]