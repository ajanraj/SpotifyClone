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
            return redirect('frontend.login')
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


@login_required(login_url='frontend.login')
def favorites(request):
    if request.is_ajax():

        if not 'action' in request.POST.keys():
            return HttpResponse(json.dumps({'key': '0', 'msg': 'Missing Parameters!'}))

        if not 'sid' in request.POST.keys():
            return HttpResponse(json.dumps({'key': '0', 'msg': 'Missing Parameters!'}))

        if request.POST['action'] == '1':

            song = Song.objects.filter(pk=request.POST['sid'])

            if not song:
                return HttpResponse(json.dumps({'key': '0', 'msg': 'Invalid Song ID!'}))
            else:
                song = song.get()

            user = CustomUser.objects.filter(pk=request.user.id)

            if not user:
                return HttpResponse(json.dumps({'key': '0', 'msg': 'Invalid User ID!'}))
            else:
                user = user.get()

            fav = Favorite(user=user, song=song)

            fav.save()

            return HttpResponse(json.dumps({'key': '1', 'msg': 'Added to Favorites!'}))

        elif request.POST['action'] == '2':

            song = Song.objects.filter(pk=request.POST['sid'])

            if not song:
                return HttpResponse(json.dumps({'key': '0', 'msg': 'Invalid Song ID!'}))
            else:
                song = song.get()

            user = CustomUser.objects.filter(pk=request.user.id)

            if not user:
                return HttpResponse(json.dumps({'key': '0', 'msg': 'Invalid User ID!'}))
            else:
                user = user.get()

            fav = Favorite.objects.filter(song=song, user=user)

            if not fav:
                return HttpResponse(json.dumps({'key': '0', 'msg': 'Not in Favorites!'}))
            else:
                fav = fav.delete()
                return HttpResponse(json.dumps({'key': '1', 'msg': 'Record Deleted!'}))


@login_required(login_url='frontend.login')
def favorites_list(request, sid):

        # Getting user Object
    user = CustomUser.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "You must Log In!")
        return redirect('frontend.login')
    else:
        user = user.get()

    # Getting all favorites song data
    fav_data = Favorite.objects.filter(user=user)

    # Getting current song data
    if find_song(sid):
        song, prev_id, next_id = find_song(sid)
    else:
        song, prev_id, next_id = find_song(random_song_id())

    # Getting if the song is in Favorite or not
    fav = Favorite.objects.filter(song=song, user=user)

    if not fav:
        fav = False
    else:
        fav = True

    return render(request, 'frontendTemplates/webplayer/favorite.html', {'fav_data': fav_data, 'song': song, 'pid': prev_id, 'nid': next_id, 'fav': fav})


@login_required(login_url='frontend.login')
def genre(request, sid):

    genre = Genre.objects.all()

    # Getting user Object
    user = CustomUser.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "You must Log In!")
        return redirect('frontend.login')
    else:
        user = user.get()

    # Getting current song data
    if find_song(sid):
        song, prev_id, next_id = find_song(sid)
    else:
        song, prev_id, next_id = find_song(random_song_id())

    # Getting if the song is in Favorite or not
    fav = Favorite.objects.filter(song=song, user=user)

    if not fav:
        fav = False
    else:
        fav = True

    return render(request, 'frontendTemplates/webplayer/genre.html', {'genre': genre, 'song': song, 'pid': prev_id, 'nid': next_id, 'fav': fav})


@login_required(login_url='frontend.login')
def genre_details(request, sid, gid):

    genre = Genre.objects.filter(pk=gid)

    if not genre:

        genre_songs = Song.objects.all()

    else:
        genre = genre.get()
        genre_songs = Song.objects.filter(genre=genre)

    # Getting user Object
    user = CustomUser.objects.filter(pk=request.user.id)

    if not user:
        messages.error(request, "You must Log In!")
        return redirect('frontend.login')
    else:
        user = user.get()

    # Getting current song data
    if find_song(sid):
        song, prev_id, next_id = find_song(sid)
    else:
        song, prev_id, next_id = find_song(random_song_id())

    # Getting if the song is in Favorite or not
    fav = Favorite.objects.filter(song=song, user=user)

    if not fav:
        fav = False
    else:
        fav = True

    return render(request, 'frontendTemplates/webplayer/genre-details.html', {'genre': genre, 'genre_songs': genre_songs, 'song': song, 'pid': prev_id, 'nid': next_id, 'fav': fav})
