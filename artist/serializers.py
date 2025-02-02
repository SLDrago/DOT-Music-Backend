# # artist/serializers.py
# from rest_framework import serializers
# from .models import Artist
# from django.contrib.auth import get_user_model


# User = get_user_model()

# class ArtistSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')

    class Meta:
        model = Artist
        fields = ['id', 'user', 'bio', 'genre', 'name']
