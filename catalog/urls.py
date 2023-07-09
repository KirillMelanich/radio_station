from django.urls import path

from .views import (
    index,
    GenreListView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
    ArtistListView,
    ArtistCreateView,
    ArtistUpdateView,
    ArtistDeleteView,
    ArtistDetailView,
    SongDeleteView,
    SongUpdateView,
    SongDetailView,
    SongCreateView,
    SongListView,
    GenreDetailView,

)

urlpatterns = [
    path("", index, name="index"),
    path("catalog/", index, name="index"),
    path(
        "genres/",
        GenreListView.as_view(),
        name="genre-list",
    ),
    path(
        "genres/create/",
        GenreCreateView.as_view(),
        name="genre-create",
    ),
    path(
        "genres/<int:pk>/",
        GenreDetailView.as_view(),
        name="genre-detail",
    )
    path(
        "genres/<int:pk>/update/",
        GenreUpdateView.as_view(),
        name="genre-update",
    ),
    path(
        "genres/<int:pk>/delete/",
        GenreDeleteView.as_view(),
        name="genre-delete",
    ),
    path(
        "artists/",
        ArtistListView.as_view(),
        name="artist-list",
    ),
    path(
        "artists/create/",
        ArtistCreateView.as_view(),
        name="artist-create",
    ),
    path(
        "artists/<int:pk>/",
        ArtistDetailView.as_view(),
        name="artist-detail",
    ),
    path(
        "artists/<int:pk>/update/",
        ArtistUpdateView.as_view(),
        name="artist-update",
    ),
    path(
        "artists/<int:pk>/delete/",
        ArtistDeleteView.as_view(),
        name="artist-delete",
    ),
    path(
        "songs/",
        SongListView.as_view(),
        name="song-list",
    ),
    path(
        "songs/create/",
        SongCreateView.as_view(),
        name="song-create",
    ),
    path(
        "songs/<int:pk>/",
        SongDetailView.as_view(),
        name="song-detail",
    ),
    path(
        "songs/<int:pk>/update/",
        SongUpdateView.as_view(),
        name="song-update",
    ),
    path(
        "songs/<int:pk>/delete/",
        SongDeleteView.as_view(),
        name="song-delete",
    ),
]

app_name = "catalog"
