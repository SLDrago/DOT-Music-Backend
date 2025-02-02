from django.http import JsonResponse
from .models import Album, PopularRadio, TodayInMusic, Songs
from artist.models import Artist


def get_lastfive_artists(request):
    artists = list(Artist.objects.select_related('user').values(
        'id', 'bio', 'genre', 'profile_picture', 'user__name'  # Fetch related User's name
    ))

    # Convert profile_picture field to a string (file path)
    for artist in artists:
        if artist['profile_picture']:  # Ensure it's not None
            artist['profile_picture'] = str(artist['profile_picture'])

    return JsonResponse({'artists': artists}, safe=False)


def get_lastfive_albums(request):
    albums = list(Album.objects.order_by('-id')[:5].values())  # Fetch last 5 records
    return JsonResponse({'albums': albums}, safe=False)

def get_lastfive_popular_radio(request):
    radios = list(PopularRadio.objects.order_by('-id')[:5].values())  # Fetch last 5 records
    return JsonResponse({'popular_radio': radios}, safe=False)

def get_lastfive_today_in_music(request):
    today_in_music = list(TodayInMusic.objects.order_by('-id')[:5].values())  # Fetch last 5 records
    return JsonResponse({'today_in_music': today_in_music}, safe=False)

# --------------------------------------------------------------------------------------

def get_artists(request):
    artists = list(Artist.objects.values())
    return JsonResponse({'artists': artists}, safe=False)

def get_albums(request):
    albums = list(Album.objects.values())
    return JsonResponse({'albums': albums}, safe=False)

def get_popular_radio(request):
    radios = list(PopularRadio.objects.values())
    return JsonResponse({'popular_radio': radios}, safe=False)

def get_today_in_music(request):
    today_in_music = list(TodayInMusic.objects.values())
    return JsonResponse({'today_in_music': today_in_music}, safe=False)


# ---------------------------------------------------------------------------------------------

# def get_songs_by_artist(request, artist_id):
#     # Fetch songs where artist matches the given artist_id
#     songs = list(Songs.objects.filter(artist_id=artist_id).values())
#     return JsonResponse({'songs': songs}, safe=False)


# def get_artist_name(request, artist_id):
#     try:
#         # Fetch the artist with the given artist_id
#         artist = Artist.objects.get(id=artist_id)
#         return JsonResponse({'artist_name': artist.name}, safe=False)  # Assuming the artist model has a 'name' field
#     except Artist.DoesNotExist:
#         return JsonResponse({'error': 'Artist not found'}, status=404)

def get_songs_by_artist(request, artist_id):
    try:
        # Fetch the artist name
        artist = Artist.objects.get(id=artist_id)
        artist_name = artist.user.name  # Assuming the Artist model has a 'name' field

        # Fetch songs where artist matches the given artist_id
        songs = list(Songs.objects.filter(artist_id=artist_id).values())

        # Return both artist name and songs
        return JsonResponse({'artist_name': artist_name, 'songs': songs}, safe=False)
    except Artist.DoesNotExist:
        return JsonResponse({'error': 'Artist not found'}, status=404)

