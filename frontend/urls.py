from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='frontend.index'),
    path('signup/', views.signup, name='frontend.signup'),
    path('login/', views.login, name='frontend.login'),
    path('login/post', views.login_post, name='frontend.login.post'),
    path('logout/', views.logout_post, name='frontend.logout'),

    path('account/', include('frontend.account.urls')),
    # path('homepage/', include('frontend.homepage.urls')),
]
