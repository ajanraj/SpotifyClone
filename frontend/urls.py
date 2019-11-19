from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='frontend.index'),
    path('signup', views.signup, name='frontend.signup'),

    # path('favorites/', include('frontend.favorite.urls')),
    # path('homepage/', include('frontend.homepage.urls')),
]
