# from django.contrib import admin
from django.conf.urls import url
from . import views
# from django.urls import path

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url('register/$', views.UserFormView.as_view(), name='index'),


    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url('album/add/$',views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/2/
    url('album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/2/delete/
    url('album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),




















    # # /music/
    # url('^$', views.index, name='index'),

    # # /music/<album_id>/
    # url(r'^(?P<album_id>[[0-9]+)/$',views.detail, name='detail'),

    #     # /music/<album_id>/favorite/
    # url(r'^(?P<album_id>[[0-9]+)/favorite/$',views.favorite, name='favorite'),

]