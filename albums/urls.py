from django.urls import path

from . import views

urlpatterns = [
#    path('', views.index, name='index'),
    path('demo1', views.demo1, name='demo1'),
    path('getAlbums', views.getAlbums, name='getAlbums'),
    path('addAlbum', views.addAlbum, name='addAlbum'),
    path('editAlbum/<int:album_id>', views.editAlbum, name='editAlbum'),
    path('deleteAlbum/<int:album_id>', views.deleteAlbum, name='deleteAlbum'),
]