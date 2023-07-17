import random

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Genre(models.Model):
    style = models.CharField(max_length=63, unique=True)
    about_genre = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["style"]

    def __str__(self):
        return f"{self.style}"

    def get_absolute_url(self):
        return reverse("catalog:genre-detail", kwargs={"pk": self.pk})


class Artist(AbstractUser):
    country = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255, default="unknown artist")

    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists"
        ordering = ["artist_name"]

    def get_absolute_url(self):
        return reverse("catalog:artist-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.username}"


class Song(models.Model):
    song = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="songs")
    artists = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="songs")
    youtube_link = models.URLField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ["song"]

    def __str__(self):
        return self.song

    def get_absolute_url(self):
        return reverse("catalog:song-detail", kwargs={"pk": self.pk})


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="playlists")
    songs = models.ManyToManyField(Song, related_name="playlists")

    class Meta:
        verbose_name = "playlist"
        verbose_name_plural = "playlists"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:playlist-detail", kwargs={"pk": self.pk})

    def generate_playlist(self, num_songs):
        """
        Generates a playlist of a particular genre with a specific number of songs.
        """
        if num_songs <= 0:
            return

        genre_songs = list(self.genre.songs.all())
        random.shuffle(genre_songs)

        if num_songs >= len(genre_songs):
            self.songs.set(genre_songs)
        else:
            self.songs.set(genre_songs[:num_songs])
