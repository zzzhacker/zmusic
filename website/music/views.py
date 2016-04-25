from django.http import HttpResponse
from .models import Album,Song
from django.shortcuts import render,get_object_or_404
from django.http import Http404

def index(request):
    all_album=Album.objects.all()
    return render(request,'music/index.html',{ 'all_album':all_album})

def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{ 'album':album})


def favourite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not select a valid song"
        })
    else:
        selected_song.is_favourite=True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})


