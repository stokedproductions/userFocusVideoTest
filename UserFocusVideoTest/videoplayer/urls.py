from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^/(?P<id>\d+)/$', views.index, name='video-viewer'),
]
