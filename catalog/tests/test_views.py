from django.contrib.auth import get_user_model
from django.test import TestCase
from catalog.forms import ArtistCreationForm
from django.urls import reverse

from catalog.models import Genre, Artist, Song

GENRE_URLS = reverse("catalog:genre-list")
ARTIST_URLS = reverse("catalog:artist-list")
SONG_URLS = reverse("catalog:song-list")


class PublicGenreTests(TestCase):
    def test_login_required(self):
        res = self.client.get(GENRE_URLS)

        self.assertNotEquals(res.status_code, 200)


class PrivateGenreTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password"
        )
        self.client.force_login(self.user)

    def test_retrieve_genre(self):
        Genre.objects.create(style="dub step")
        Genre.objects.create(style="doom")

        response = self.client.get(GENRE_URLS)
        genres = Genre.objects.all()

        self.assertEqual(
            list(response.context["genre_list"]),
            list(genres)
        )
        self.assertTemplateUsed(response, "catalog/genre_list.html")


class PublicArtistTests(TestCase):
    def test_login_required(self):
        res = self.client.get(ARTIST_URLS)

        self.assertNotEquals(res.status_code, 200)


class PrivateArtistTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password"
        )
        self.client.force_login(self.user)

    def test_retrieve_artist(self):
        Artist.objects.create(username="radiohead")
        Artist.objects.create(username="will_smith")

        response = self.client.get(ARTIST_URLS)
        artists = Artist.objects.all()

        self.assertEqual(
            list(response.context["artist_list"]),
            list(artists)
        )
        self.assertTemplateUsed(response, "catalog/artist_list.html")


class PublicArtistTests(TestCase):
    def test_login_required(self):
        res = self.client.get(ARTIST_URLS)

        self.assertNotEquals(res.status_code, 200)

