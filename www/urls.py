from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'^$map.html', views.map, name='map'),
]
=======
    url(r'^$', views.homepage, name='homepage'),
]
>>>>>>> 350f01929fa51bc30c894ff065e26174b5be43d8
