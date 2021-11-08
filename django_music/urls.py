"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# had to modify this to add the 'include' functionality as well
from django.urls import include, path

# added this to tell it to use albums.views
from albums import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo1', views.demo1, name='demo1'),
    path('getAlbums', views.getAlbums, name='getAlbums'),
    path('addAlbum', views.addAlbum, name='addAlbum'),
    path('editAlbum/<int:album_id>', views.editAlbum, name='editAlbum'),
    path('deleteAlbum/<int:album_id>', views.deleteAlbum, name='deleteAlbum'),
    # here we're specifying that top level path should use the albums.urls paths
#    path('', include('albums.urls')),
    # here we're using the default admin site urls path (for django-powered auth mgmt)
    path('admin/', admin.site.urls),
]

