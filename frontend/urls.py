from django.urls import path, include
from . import views
urlpatterns = [
    # path('', include('social_django.urls', namespace='social')),
    path('', views.index, name='frontend.index'),
    path('signup/', views.signup, name='frontend.signup'),
    path('login/', views.login, name='frontend.login'),
    path('login/post', views.login_post, name='frontend.login.post'),
    path('logout/', views.logout_post, name='frontend.logout'),

    path('account/', include('frontend.account.urls')),
    path('webplayer/', include('frontend.webplayer.urls')),
]
