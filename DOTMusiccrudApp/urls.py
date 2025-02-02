from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.get_lastfive_artists, name='get_artists'),
    path('albums/', views.get_lastfive_albums, name='get_albums'),
    path('popular-radio/', views.get_lastfive_popular_radio, name='get_popular_radio'),
    path('today-in-music/', views.get_lastfive_today_in_music, name='get_today_in_music'),
    path('full-artists/', views.get_artists, name='get_full_artists'),
    path('full-albums/', views.get_lastfive_albums, name='get_full_albums'),
    path('full-radio/', views.get_popular_radio, name='get_popular_radio'),
    path('songs/artist/<int:artist_id>/', views.get_songs_by_artist, name='get_songs_by_artist'),
]