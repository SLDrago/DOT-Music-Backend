from django.db import models
from artist.models import Artist

class Song(models.Model):
    GENRES = [
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

    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name='artist_songs', on_delete=models.CASCADE)  # Updated related_name
    genre = models.CharField(max_length=50, choices=GENRES)
    release_date = models.DateField()
    bio = models.TextField()
    audio_file = models.FileField(upload_to='songs/%Y/%m/%d/')
    cover_image = models.ImageField(upload_to='songs/covers/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.title
