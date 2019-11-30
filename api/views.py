from django.shortcuts import render
from rest_framework import viewsets
from .serializer import SongSerializer
from admin.song .models import Song
# Create your views here.


class SongViewSets(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
