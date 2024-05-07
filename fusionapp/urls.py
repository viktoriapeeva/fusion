from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('feed', views.feed, name='feed'),
    path('user-profile', views.user_profile, name='user-profile'),

    path('view-post/<int:pk>', views.view_post, name='view-post'),
    path('create-post', views.create_post, name='create-post'),
    path('update-post/<int:pk>', views.update_post, name='update-post'),
    path('delete-post/<int:pk>', views.delete_post, name='delete-post'),


]