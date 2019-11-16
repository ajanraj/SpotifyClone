from django.db import models
from admin.genre.models import Genre
from admin.moods.models import Moods
from admin.artists.models import Artists
# Create your models here.


class Song(models.Model):

    song_name = models.CharField(max_length=100)
    song_des = models.CharField(
        max_length=250, default="This is a Popular Song!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    song_length = models.CharField(max_length=10)
    song_file = models.FileField(upload_to='songs/')

    # foreign key

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    mood = models.ForeignKey(Moods, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name
