from django.urls import path
from .views import Songslist,PlaylistDetails,CreatePlaylist,UserSongslist,UpdatePlaylist,DeletePlaylist,UserLogin,Register,UserProfile,CreateProfile#,AddPush
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path("",Songslist.as_view(),name="home"),
    path("login/",UserLogin.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page="home"),name="logout"),
    path('register/',Register.as_view(),name='register'),

    path('create-profile/',CreateProfile.as_view(),name='create-profile'),
    path('profile/',UserProfile.as_view(),name='profile'),
    path('embed_help/',views.embed_code_help,name='embed_code_help'),


    path("playlist/<int:pk>/like",views.PushView,name="push"),
    path("playlist-detail/<int:pk>/",PlaylistDetails.as_view(),name="playlist_details"),
    path("playlist-create/",CreatePlaylist.as_view(), name="playlist_create"),
    path("posted-playlist/",UserSongslist.as_view() , name="posted_playlist"),
    path("playlist-update/<int:pk>/",UpdatePlaylist.as_view(),name="playlist_update"),
    path("playlist-delete/<int:pk>/",DeletePlaylist.as_view(), name="playlist_delete")
]