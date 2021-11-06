#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from albums.models import Album
from django.template import loader
from .forms import AlbumForm
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the albums index.")

def demo1(request):
    return HttpResponse("Hello, demo1!")

def getAlbums(request):
    albums = list(Album.objects.values())
    return JsonResponse({'albums':albums});
#    html = ""
#    albums = Album.objects.all()
#    for a in albums:
#        html = html + a.title + "<br />"
#    return HttpResponse(html)


def addAlbum(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/getAlbums')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()
        return render(request, 'albums/addAlbum.html', {'form': form})

