from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Genre(models.Model):
    style = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["style"]

    def __str__(self):
        return f"{self.style}"


class Artist(AbstractUser):
    country = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255, default="Solo artist")
    youtube_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists"

    def get_absolute_url(self):
        return reverse("catalog:artist-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.username}"


class Song(models.Model):
    song = models.CharField(max_length=255)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="songs"
    )
    artists = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="songs")
    youtube_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.song

    def get_absolute_url(self):
        return reverse("catalog:song-detail", kwargs={"pk": self.pk})
