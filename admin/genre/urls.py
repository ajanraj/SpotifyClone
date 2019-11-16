from django.urls import path, include
from .import views

urlpatterns = [
    path('add', views.add, name='admin.genre.add'),
    path('save', views.save, name='admin.genre.save'),
    path('index', views.index, name='admin.genre.index'),
    path('delete/<int:id>', views.delete, name='admin.genre.delete'),
    path('edit/<int:id>', views.edit, name='admin.genre.edit'),
    path('update/<int:id>', views.update, name='admin.genre.update'),

]
