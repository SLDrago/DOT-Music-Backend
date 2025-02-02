from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Song
from .serializers import SongSerializer
from rest_framework.generics import ListAPIView

class SongListView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get(self, request):
        # Filter songs by the logged-in artist
        songs = Song.objects.filter(artist=request.user.artist_profile)
        serializer = SongSerializer(songs, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class SongUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SongSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(artist=request.user.artist_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            song = Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return Response({"error": "Song not found"}, status=status.HTTP_404_NOT_FOUND)

        if song.artist.user != request.user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

        serializer = SongSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            song = Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return Response({"error": "Song not found"}, status=status.HTTP_404_NOT_FOUND)

        if song.artist.user != request.user:
            return Response({"error": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

        song.delete()
        return Response({"message": "Song deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
