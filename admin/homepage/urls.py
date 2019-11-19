from django.urls import path, include
from .import views

urlpatterns = [
    path('add', views.add, name='admin.homepage.add'),
    path('save', views.save, name='admin.homepage.save'),
    path('index', views.index, name='admin.homepage.index'),
    path('delete/<int:id>', views.delete, name='admin.homepage.delete'),
    path('edit/<int:id>', views.edit, name='admin.homepage.edit'),
    path('update/<int:id>', views.update, name='admin.homepage.update'),

]
