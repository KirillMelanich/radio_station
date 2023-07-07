from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    context_object_name = "genre_list"
    template_name = "catalog/genre_list.html"
    paginate_by = 5
    queryset = Genre.objects.all()


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("catalog:genre-list")


class ArtistListView(LoginRequiredMixin, generic.ListView):
    model = Artist
    context_object_name = "artist_list"
    template_name = "catalog/artist_list.html"
    paginate_by = 5
    queryset = Artist.objects.all()


class ArtistDetailView(LoginRequiredMixin, generic.DetailView):
    model = Artist
    queryset = Artist.objects.all().prefetch_related("songs__artist")


class ArtistCreateView(LoginRequiredMixin, generic.CreateView):
    model = Artist
    fields = "__all__"
    success_url = reverse_lazy("catalog:artist-list")


class ArtistUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Artist
    fields = "__all__"
    success_url = reverse_lazy("catalog:artist-list")


class ArtistDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Artist
    success_url = reverse_lazy("catalog:artist-list")