from django.db import models
from admin.song.models import Song

# Create your models here.


class Homepage(models.Model):

    title = models.CharField(max_length=50)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
