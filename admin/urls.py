from django.urls import path, include

urlpatterns = [
    path('', include('admin.login.urls')),
    path('dashboard/', include('admin.dashboard.urls')),
    path('genre/', include('admin.genre.urls')),
    path('moods/', include('admin.moods.urls')),
    path('artists/', include('admin.artists.urls')),
    path('song/', include('admin.song.urls')),
    path('users/', include('admin.user.urls')),
    path('favorites/', include('admin.favorite.urls')),
    path('homepage/', include('admin.homepage.urls')),
]
