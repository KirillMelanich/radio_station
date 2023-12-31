from django.urls import path

from .views import (
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
    BaseView,
    PlaylistListView,
    PlaylistDetailView,
    GeneratePlaylistView,
)

urlpatterns = [
    path("", BaseView.as_view(), name="index"),
    path("catalog/", BaseView.as_view(), name="index"),
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
    ),
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
    path("playlists/", PlaylistListView.as_view(), name="playlist-list"),
    path("playlist/<int:pk>/", PlaylistDetailView.as_view(), name="playlist-detail"),
    path(
        "generate_playlist/", GeneratePlaylistView.as_view(), name="generated-playlist"
    ),
]


app_name = "catalog"
