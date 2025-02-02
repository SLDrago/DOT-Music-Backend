from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.user.username', read_only=True)

    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['artist']
