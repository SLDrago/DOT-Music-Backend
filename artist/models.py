from django.db import models
from users.models import User  # Import User model

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="artist_profile")  # Link to User model
    bio = models.TextField()  # Brief biography
    profile_picture = models.ImageField(upload_to='artist_Pic/', blank=True, null=True)  # Optional profile picture
    genre = models.CharField(max_length=100, blank=True, null=True)  # Genre (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the artist is created

    def __str__(self):
        return self.user.name  # Return the linked user's name
