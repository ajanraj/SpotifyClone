from django.shortcuts import render, redirect
from admin.homepage.models import Homepage
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, logout, login as auth_login
from admin.user.models import CustomUser
from admin.homepage.models import Homepage
from admin.song.models import Song
from admin.user.models import CustomUser
from admin.genre.models import Genre
from admin.moods.models import Moods
from admin.artists.models import Artists
from admin.favorite.models import Favorite
import random
import json


def find_song(song_id):

    song = Song.objects.filter(pk=song_id)

    if not song:
        return False
    else:
        song = song.get()

    song_ids = Song.objects.values_list('id', flat=True)

    sid_index = list(song_ids).index(song_id)

    if sid_index == 0:

        prev_id = '-1'
        next_id = str(song_ids[sid_index+1])

    elif sid_index == len(song_ids) - 1:

        prev_id = str(song_ids[sid_index-1])
        next_id = '-1'

    else:
        prev_id = str(song_ids[sid_index-1])
        next_id = str(song_ids[sid_index+1])

    return song, prev_id, next_id


def random_song_id():
    song_ids = Song.objects.values_list('id', flat=True)

    return random.choice(list(song_ids))


@login_required(login_url='frontend.login')
def index(request):

    return redirect('player-index-id', sid=random_song_id())


@login_required(login_url='frontend.login')
def index_id(request, sid):

    data = Homepage.objects.all()

    if find_song(sid):
        song, prev_id, next_id = find_song(sid)

        song = Song.objects.filter(pk=sid)

        if not song:
            return redirect('player-index-id', sid=random_song_id())
        else:
            song = song.get()

        user = CustomUser.objects.filter(pk=request.user.id)

        if not user:
            return redirect('home-login')
        else:
            user = user.get()

        fav = Favorite.objects.filter(song=song, user=user)

        if not fav:
            fav = False
        else:
            fav = True
    else:
        return redirect('player-index-id', sid=random_song_id())

    return render(request, 'frontendTemplates/webplayer/index.html', {'data': data, 'song': song, 'pid': prev_id, 'nid': next_id, 'fav': fav})
