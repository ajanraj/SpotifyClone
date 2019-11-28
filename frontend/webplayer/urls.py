from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='frontend.webplayer.index'),
    path('<int:sid>/', views.index_id, name='player-index-id'),
    path('addtofavorites/', views.favorites, name='player-favorites-add'),
    path('favorites/<int:sid>/', views.favorites_list, name='player-favorites'),
    path('genre/<int:sid>/', views.genre, name='player-genre'),
    path('genre/songs/<int:sid>/<int:gid>',
         views.genre_details, name='player-genre-details'),

]
