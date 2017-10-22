from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^map/?$', views.map, name='map'),
    url(r'^add-event/?$', views.add_event, name='add_event'),
    url(r'^event_page/?$', views.event_page, name='event_page'),
]

