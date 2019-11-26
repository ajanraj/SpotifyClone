from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='frontend.account.index'),
    path('edit/', views.edit, name='frontend.account.edit'),
    path('update/', views.update, name='frontend.account.update'),
    path('update/password', views.update_pass,
         name='frontend.account.update.pass'),
    path('edit/password/', views.edit_pass, name='frontend.account.edit.pass'),
    path('update/profile-pic', views.change_profile_pic,
         name='frontend.account.pic.upload'),
    path('privacy', views.privacy, name='frontend.privacy'),
    path('subscription', views.subscription, name='frontend.subscription'),

]
