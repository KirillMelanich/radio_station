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
        "artists/<int:pk>/update/",
        ArtistUpdateView.as_view(),
        name="artist-update",
    ),
    path(
        "artists/<int:pk>/delete/",
        ArtistDeleteView.as_view(),
        name="artist-delete",
    ),
]

app_name = "catalog"
