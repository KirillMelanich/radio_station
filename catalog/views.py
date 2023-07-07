from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from catalog.models import Artist, Song, Genre


@login_required
def index(request):
    """View function for the home page of the site."""

    num_artists = Artist.objects.count()
    num_songs = Song.objects.count()
    num_genres = Genre.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_artists": num_artists,
        "num_songs": num_songs,
        "num_genres": num_genres,
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)