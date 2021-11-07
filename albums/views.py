#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from albums.models import Album
from django.template import loader
from .forms import AlbumForm
from django.shortcuts import render
from django.utils import timezone

def index(request):
    return HttpResponse("Hello, world. You're at the albums index.")

def demo1(request):
    return HttpResponse("Hello, demo1!")

def getAlbums(request):
    albums = list(Album.objects.values())
#    return JsonResponse({'albums':albums});
    return render(request, 'albums/albums.html', {'albums':albums})


def editAlbum(request, album_id):
    # if this is a POST request we need to process the form data
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        album.title = request.POST['title']
        album.artist = request.POST['artist']
        album.save()
        return HttpResponseRedirect('/getAlbums')
#        return HttpResponseRedirect('/editAlbum/'+str(album_id))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()
        return render(request, 'albums/editAlbum.html', {'form': form, 'album':album})


def addAlbum(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
#            return JsonResponse(data)
            q = Album(title=data['title'], artist=data['artist'], created_at=timezone.now())
            q.save()
            return HttpResponseRedirect('/getAlbums')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()
        return render(request, 'albums/addAlbum.html', {'form': form})

