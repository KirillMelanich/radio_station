from django.urls import path

from .views import (
    index,

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
]

app_name = "catalog"
