# artist/urls.py
from django.urls import path
from .views import ArtistLoginView, ArtistTypeView, ArtistRegisterView

urlpatterns = [
    path('login/', ArtistLoginView.as_view(), name='artist-login'),
    path('types/', ArtistTypeView.as_view(), name='artist-types'),  # Endpoint for artist types
    path('register/', ArtistRegisterView.as_view(), name='artist-register'),  # New endpoint for registration
]
