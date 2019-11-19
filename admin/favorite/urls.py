from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='admin.favorite.index'),
    path('index/<int:id>', views.index_id, name='admin.favorite.index-id'),
]
