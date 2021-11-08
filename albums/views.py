#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import AlbumForm
from django.shortcuts import render
from albums.models import Album
from django.utils import timezone

def index(request):
    return getAlbums(request)
#    return HttpResponse("Hello, world. You're at the albums index.")

def demo1(request):
    return HttpResponse("Hello, demo1!")

def getAlbums(request):
    albums = list(Album.objects.values())
    # Used this resource to sort a list of dictionary entries by a specific key:
    # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
    albums = sorted(albums, key=lambda d: d['title'])

#    return JsonResponse({'albums':albums});
    return render(request, 'albums/albums.html', {'albums':albums})


def editAlbum(request, album_id):
    # if this is a POST request we need to process the form data
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            album.title = data['title']
            album.artist = data['artist']
            album.save()
        return HttpResponseRedirect('/getAlbums')
        # return HttpResponseRedirect('/editAlbum/'+str(album_id))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()
        return render(request, 'albums/editAlbum.html', {'form': form, 'album':album})


def addAlbum(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        ## Simple version:
        q = Album(title=request.POST['title'], artist=request.POST['artist'], created_at=timezone.now())
        q.save()
        return HttpResponseRedirect('/getAlbums')
        ## Version using Django forms.py functionality
        #form = AlbumForm(request.POST)
        #if form.is_valid():
        #    data = form.cleaned_data
        #    q = Album(title=data['title'], artist=data['artist'], created_at=timezone.now())
        #    q.save()
        #    return HttpResponseRedirect('/getAlbums')

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'albums/addAlbum.html')

def deleteAlbum(request, album_id):
    album = Album.objects.get(id=album_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        album.delete();
        return HttpResponseRedirect('/getAlbums')
    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'albums/deleteAlbum.html', {'album':album})

