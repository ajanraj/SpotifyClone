from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from admin.moods.models import Moods
from admin.artists.models import Artists
from admin.genre.models import Genre
from admin.song.models import Song
# Create your views here.


@login_required(login_url='admin.login')
def add(request):
    genre = Genre.objects.all
    mood = Moods.objects.all
    artist = Artists.objects.all
    return render(request, 'adminTemplates/song/song-add.html', {'genre': genre, 'mood': mood, 'artist': artist})


@login_required(login_url='admin.login')
def save(request):
    if request.method == 'POST':

        if not 'name' in request.POST.keys():
            messages.error(request, "Parameters are missing")
            return redirect("admin.song.add")

        if not 'description' in request.POST.keys():
            messages.error(request, "Parameters are missing")
            return redirect("admin.song.add")

        if not 'length' in request.POST.keys():
            messages.error(request, "Parameters are missing")
            return redirect("admin.song.add")

        if not 'genre' in request.POST.keys():
            messages.error(request, "Parameters are missing")
            return redirect("admin.song.add")

        if not 'mood' in request.POST.keys():
            messages.error(request, "Parameters are missing")
            return redirect("admin.song.add")

        if not 'artist' in request.POST.keys():
            messages.error(request, "Parameters are missing")
            return redirect("admin.song.add")

        if not 'file' in request.FILES.keys():
            messages.error(request, "Parameters are missing")
            return redirect("admin.song.add")

        name = request.POST['name']
        description = request.POST['description']
        length = request.POST['length']
        mood = request.POST['mood']
        artist = request.POST['artist']
        genre = request.POST['genre']
        song_file = request.FILES['file']

        if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', name):
            messages.error(request, "Enter a valid name!")
            return redirect("admin.song.add")

        if not re.match('^[(a-z)?(A-Z)?\d?!?_?\-?\.?\,?\s?]+$', description):
            messages.error(request, "Enter a valid Description!")
            return redirect("admin.song.add")

        if not re.match('^\d{2}:\d{2}$', length):
            messages.error(request, "Enter a valid length!")
            return redirect("admin.song.add")

        if genre == "-1":
            messages.error(request, "Select a genre Option!")
            return redirect("admin.song.add")

        if mood == "-1":
            messages.error(request, "Select a mood Option!")
            return redirect("admin.song.add")

        if artist == "-1":
            messages.error(request, "Select an artist Option!")
            return redirect("admin.song.add")

        file_extension = song_file.name.split('.')[-1]

        if not file_extension.lower() in ['mp3', 'wav']:
            messages.error(request, "Select a valid File!")
            return redirect("admin.song.add")

        genre = Genre.objects.filter(pk=genre)

        if not genre:
            messages.error(request, "Select a valid Genre")
            return redirect("admin.song.add")
        else:
            genre = genre.get()

        mood = Moods.objects.filter(pk=mood)

        if not mood:
            messages.error(request, "Select a valid Mood")
            return redirect("admin.song.add")
        else:
            mood = mood.get()

        artist = Artists.objects.filter(pk=artist)

        if not artist:
            messages.error(request, "Select a valid Artist")
            return redirect("admin.song.add")
        else:
            artist = artist.get()

        songObj = Song(song_name=name, song_des=description,
                       song_length=length, genre=genre, mood=mood, artist=artist, song_file=song_file)

        songObj.save()

        messages.success(request, "Data Added successfully")
        return redirect("admin.song.index")

    else:
        return redirect("admin.song.add")


@login_required(login_url='admin.login')
def index(request):
    if request.method == 'GET':

        data = Song.objects.all()

        return render(request, 'adminTemplates/song/index.html', {'data': data})


@login_required(login_url='admin.login')
def delete(request, id):
    if request.method == 'GET':

        song = Song.objects.filter(pk=id)

        if not song:
            messages.error(request, "No Such songs found!")
            return redirect("admin.song.index")

        else:
            # Deleting song file
            song_obj = song.get()
            song_obj.song_file.delete()
            # Deleting song record from database
            song.delete()

            messages.success(request, "Record Deleted!")
            return redirect("admin.song.index")


@login_required(login_url='admin.login')
def edit(request, id):
    if request.method == 'GET':

        song = Song.objects.filter(pk=id)

        if not song:
            messages.error(request, "No Such songs found!")
            return redirect("admin.song.index")

        else:
            song = song.get()

            genre = Genre.objects.all()
            artist = Artists.objects.all()
            mood = Moods.objects.all()

            return render(request, 'adminTemplates/song/edit.html', {'genre': genre, 'song': song, 'mood': mood, 'artist': artist})


@login_required(login_url='admin.login')
def update(request, id):

    if request.method == 'POST':

        if not 'name' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('admin.song.index')

        if not 'description' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('admin.song.index')

        if not 'length' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('admin.song.index')

        if not 'genre' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('admin.song.index')

        if not 'mood' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('admin.song.index')

        if not 'artist' in request.POST.keys():
            messages.error(request, "Parameters are missing!")
            return redirect('admin.song.index')

        name = request.POST['name']
        description = request.POST['description']
        length = request.POST['length']
        genre = request.POST['genre']
        mood = request.POST['mood']
        artist = request.POST['artist']

        if not re.match('^[(a-z)?(A-Z)?\d?_?\-?\.?\,?\s?]+$', name):
            messages.error(request, "Enter a valid name!")
            return redirect("admin.song.index")

        if not re.match('^[(a-z)?(A-Z)?\d?_?!?\-?\.?\,?\s?]+$', description):
            messages.error(request, "Enter a valid description!")
            return redirect("admin.song.index")

        if not re.match('^\d{2}:\d{2}$', length):
            messages.error(request, "Enter a valid length!")
            return redirect("admin.song.index")

        if genre == "-1":
            messages.error(request, "Select a genre option!")
            return redirect("admin.song.index")

        if mood == "-1":
            messages.error(request, "Select a mood option!")
            return redirect("admin.song.index")

        if artist == "-1":
            messages.error(request, "Select an artist option!")
            return redirect("admin.song.index")

        genre = Genre.objects.filter(pk=genre)
        if not genre:
            messages.error(request, "Select a valid Genre!")
            return redirect("admin.song.index")
        else:
            genre = genre.get()

        mood = Moods.objects.filter(pk=mood)
        if not mood:
            messages.error(request, "Select a valid Mood!")
            return redirect("admin.song.index")
        else:
            mood = mood.get()

        artist = Artists.objects.filter(pk=artist)
        if not artist:
            messages.error(request, "Select a valid Artist!")
            return redirect("admin.song.index")
        else:
            artist = artist.get()

        song = Song.objects.filter(pk=id)

        if not song:
            messages.error(request, "No such songs!")
            return redirect("admin.song.index")
        else:
            song = song.get()

        if 'file' in request.FILES.keys():
            song_file = request.FILES['file']

            file_extension = song_file.name.split('.')[-1]

            if not file_extension.lower() in ['mp3', 'wav']:
                messages.error(request, "Select a valid file!")
                return redirect("admin.song.index")

            song.song_file.delete()

            song.song_name = name

            song.song_des = description

            song.song_length = length

            song.genre = genre

            song.mood = mood

            song.artist = artist

            song.song_file = song_file

            song.save()

            messages.error(request, "Record Updated!")
            return redirect("admin.song.index")

        else:
            song.song_name = name

            song.song_des = description

            song.song_length = length

            song.genre = genre

            song.mood = mood

            song.artist = artist

            song.save()

            messages.error(request, "Record Updated!")
            return redirect("admin.song.index")


@login_required(login_url='admin.login')
def details(request, id):

    if request.method == 'GET':

        song = Song.objects.filter(pk=id)

        if not song:
            messages.error(request, "No such songs!")
            return redirect("admin.song.index")
        else:
            song = song.get()

        return render(request, 'adminTemplates/song/details.html', {'song': song})
