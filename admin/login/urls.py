from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.index, name='admin.login'),
    path('login', views.login, name='admin.login.post'),
    path('logout', views.logout_now, name='admin.logout'),
]
