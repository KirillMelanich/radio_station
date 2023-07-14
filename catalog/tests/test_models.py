from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from catalog.models import Genre, Song, Artist


class GenreModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(style="Rock")

    def test_genre_style(self):
        self.assertEqual(self.genre.style, "Rock")

    def test_genre_about_genre(self):
        self.assertIsNone(self.genre.about_genre)

    def test_genre_str_method(self):
        self.assertEqual(str(self.genre), "Rock")

    def test_genre_absolute_url(self):
        expected_url = reverse("catalog:genre-detail", kwargs={"pk": self.genre.pk})
        self.assertEqual(self.genre.get_absolute_url(), expected_url)


class ArtistModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(
            username="john", artist_name="John Doe", country="USA"
        )

    def test_artist_username(self):
        self.assertEqual(self.artist.username, "john")

    def test_artist_artist_name(self):
        self.assertEqual(self.artist.artist_name, "John Doe")

    def test_artist_country(self):
        self.assertEqual(self.artist.country, "USA")

    def test_artist_str_method(self):
        self.assertEqual(str(self.artist), "john")

    def test_artist_absolute_url(self):
        expected_url = reverse("catalog:artist-detail", kwargs={"pk": self.artist.pk})
        self.assertEqual(self.artist.get_absolute_url(), expected_url)


class SongModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(style="Rock")
        self.artist = Artist.objects.create(
            username="john", artist_name="John Doe", country="USA"
        )
        self.song = Song.objects.create(song="Song 1", genre=self.genre)
        self.song.artists.add(self.artist)  # Add the artist to the artists field

    def test_song_song(self):
        self.assertEqual(self.song.song, "Song 1")

    def test_song_genre(self):
        self.assertEqual(self.song.genre, self.genre)

    def test_song_artists(self):
        self.assertEqual(list(self.song.artists.all()), [self.artist])

    def test_song_youtube_link(self):
        self.assertIsNone(self.song.youtube_link)

    def test_song_str_method(self):
        self.assertEqual(str(self.song), "Song 1")

    def test_song_absolute_url(self):
        expected_url = reverse("catalog:song-detail", kwargs={"pk": self.song.pk})
        self.assertEqual(self.song.get_absolute_url(), expected_url)
