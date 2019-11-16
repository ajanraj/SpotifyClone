from django.urls import path, include
from .import views

urlpatterns = [
    path('add', views.add, name='admin.artists.add'),
    path('save', views.save, name='admin.artists.save'),
    path('index', views.index, name='admin.artists.index'),
    path('delete/<int:id>', views.delete, name='admin.artists.delete'),
    path('edit/<int:id>', views.edit, name='admin.artists.edit'),
    path('update/<int:id>', views.update, name='admin.artists.update'),

]
