from django.test import TestCase
from catalog.forms import ArtistCreationForm, SongForm, GenreForm, SongSearchForm, ArtistSearchForm, GenreSearchForm


class ArtistCreationFormTest(TestCase):
    def test_artist_creation_form_valid_data(self):
        form = ArtistCreationForm(data={
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'artist_name': 'John Doe',
            'country': 'USA'
        })
        self.assertTrue(form.is_valid())

    def test_artist_creation_form_invalid_data(self):
        form = ArtistCreationForm(data={
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'mismatchpassword',
            'artist_name': 'John Doe',
            'country': 'USA'
        })
        self.assertFalse(form.is_valid())

    def test_artist_creation_form_missing_data(self):
        form = ArtistCreationForm(data={})
        self.assertFalse(form.is_valid())


class SongFormTest(TestCase):
    def test_song_form_invalid_data(self):
        form = SongForm(data={
            'song': 'Test Song',
            'genre': 1,
            'artists': []
        })
        self.assertFalse(form.is_valid())


class GenreFormTest(TestCase):
    def test_genre_form_valid_data(self):
        form = GenreForm(data={
            'style': 'Test Genre'
        })
        self.assertTrue(form.is_valid())

    def test_genre_form_invalid_data(self):
        form = GenreForm(data={
            'style': ''
        })
        self.assertFalse(form.is_valid())


class SongSearchFormTest(TestCase):
    def test_song_search_form_valid_data(self):
        form = SongSearchForm(data={
            'song': 'Test Song'
        })
        self.assertTrue(form.is_valid())

    def test_song_search_form_invalid_data(self):
        form = SongSearchForm(data={
            'song': ''
        })
        self.assertTrue(form.is_valid())


class ArtistSearchFormTest(TestCase):
    def test_artist_search_form_valid_data(self):
        form = ArtistSearchForm(data={
            'artist_name': 'John Doe'
        })
        self.assertTrue(form.is_valid())

    def test_artist_search_form_invalid_data(self):
        form = ArtistSearchForm(data={
            'artist_name': ''
        })
        self.assertTrue(form.is_valid())


class GenreSearchFormTest(TestCase):
    def test_genre_search_form_valid_data(self):
        form = GenreSearchForm(data={
            'style': 'Test Genre'
        })
        self.assertTrue(form.is_valid())

    def test_genre_search_form_invalid_data(self):
        form = GenreSearchForm(data={
            'style': ''
        })
        self.assertTrue(form.is_valid())