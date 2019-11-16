from django.urls import path, include
from .import views

urlpatterns = [
    path('add', views.add, name='admin.moods.add'),
    path('save', views.save, name='admin.moods.save'),
    path('index', views.index, name='admin.moods.index'),
    path('delete/<int:id>', views.delete, name='admin.moods.delete'),
    path('edit/<int:id>', views.edit, name='admin.moods.edit'),
    path('update/<int:id>', views.update, name='admin.moods.update'),

]
