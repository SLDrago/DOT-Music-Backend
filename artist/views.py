from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ArtistSerializer
from django.contrib.auth import authenticate

# Get the custom User model
User = get_user_model()


class ArtistRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get('username')  # Assuming you're using 'name' instead of 'username'
        password = request.data.get('password')
        email = request.data.get('email')
        bio = request.data.get('bio', '')
        genre = request.data.get('artist_type', 'pop')

        # Check if name and password are provided
        if not name or not password:
            return Response({"error": "Name and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user using the custom user model (adjusting to 'name')
        user = User.objects.create_user(name=name, password=password, email=email)

        # Create a new artist linked to the user
        artist = Artist.objects.create(user=user, bio=bio, genre=genre)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Serialize the artist data
        artist_data = ArtistSerializer(artist).data

        return Response({
            'message': 'Registration successful',
            'artist': artist_data,
            'access_token': access_token,  # Add access token
            'refresh_token': refresh_token  # Add refresh token
        }, status=status.HTTP_201_CREATED)


class ArtistLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        
        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            artist = user.artist_profile  # Get the artist profile using the related_name
        except Artist.DoesNotExist:
            return Response({"error": "User is not registered as an artist"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Serialize artist data
        artist_data = ArtistSerializer(artist).data

        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'name': user.name,  # Corrected from username to name
            'artistId': artist.id,
            'artist': artist_data
        }, status=status.HTTP_200_OK)

class ArtistTypeView(APIView):
    permission_classes = [IsAuthenticated]  # Optional, if you need authentication
    
    ARTIST_TYPES = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('hip_hop', 'Hip-Hop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('reggae', 'Reggae'),
        ('electronic', 'Electronic'),
        ('country', 'Country'),
        ('blues', 'Blues'),
        ('metal', 'Metal'),
    ]
    
    def get(self, request):
        # Return artist types as JSON response
        artist_types = [{"value": value, "label": label} for value, label in self.ARTIST_TYPES]
        return Response(artist_types, status=status.HTTP_200_OK)
