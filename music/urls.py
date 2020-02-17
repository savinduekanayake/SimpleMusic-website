# from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url('^$', views.index, name='index'),

    # /music/71/
    url(r'^(?P<album_id>[[0-9]+)/$',views.detail, name='detail'),

]