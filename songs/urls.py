# songs/urls.py
from django.urls import path
from .views import SongListView, SongUploadView, SongUpdateView, SongDeleteView

urlpatterns = [
    path('', SongListView.as_view(), name='song-list'),            # List all songs
    path('upload/', SongUploadView.as_view(), name='song-upload'),  # Upload a new song
    path('<int:pk>/update/', SongUpdateView.as_view(), name='song-update'),  # Update a song
    path('<int:pk>/delete/', SongDeleteView.as_view(), name='song-delete'),  # Delete a song
]
