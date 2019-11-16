from django.urls import path, include
from .import views

urlpatterns = [
    path('add', views.add, name='admin.song.add'),
    path('save', views.save, name='admin.song.save'),
    path('index', views.index, name='admin.song.index'),
    path('delete/<int:id>', views.delete, name='admin.song.delete'),
    path('edit/<int:id>', views.edit, name='admin.song.edit'),
    path('update/<int:id>', views.update, name='admin.song.update'),
    path('details/<int:id>', views.details, name='admin.song.details'),

]
