from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import SongForm, SongSearchForm, ArtistSearchForm, GenreForm
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


class GenreDetailView(LoginRequiredMixin, generic.DetailView):
    model = Genre
    queryset = Genre.objects.all()


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    form = GenreForm
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    form = GenreForm
    fields = "__all__"
    success_url = reverse_lazy("catalog:genre-list")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("catalog:genre-list")


class ArtistListView(LoginRequiredMixin, generic.ListView):
    model = Artist
    context_object_name = "artist_list"
    template_name = "catalog/artist_list.html"
    paginate_by = 10
    queryset = Artist.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)

        artist_name = self.request.GET.get("artist_name", "")

        context["search_form"] = ArtistSearchForm(
            initial={
                "artist_name": artist_name
            }
        )

        return context

    def get_queryset(self):
        queryset = Artist.objects.select_related(None)
        form = ArtistSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                artist_name__icontains=form.cleaned_data["artist_name"],
            )

        return queryset


class ArtistDetailView(LoginRequiredMixin, generic.DetailView):
    model = Artist
    queryset = Artist.objects.all().prefetch_related("songs__genre")


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


class SongListView(LoginRequiredMixin, generic.ListView):
    model = Song
    context_object_name = "song_list"
    template_name = "catalog/song_list.html"
    paginate_by = 10
    queryset = Song.objects.select_related("genre")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SongListView, self).get_context_data(**kwargs)

        song = self.request.GET.get("song", "")

        context["search_form"] = SongSearchForm(
            initial={
                "song": song
            }
        )

        return context

    def get_queryset(self):
        queryset = Song.objects.select_related("genre")
        form = SongSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                song__icontains=form.cleaned_data["song"],
            )

        return queryset


class SongDetailView(LoginRequiredMixin, generic.DetailView):
    model = Song


class SongCreateView(LoginRequiredMixin, generic.CreateView):
    model = Song
    form = SongForm
    fields = "__all__"
    # success_url = reverse_lazy("catalog:song-list")


class SongUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Song
    fields = "__all__"
    success_url = reverse_lazy("catalog:song-list")


class SongDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Song
    success_url = reverse_lazy("catalog:song-list")
