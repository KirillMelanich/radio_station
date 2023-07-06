from django.db import models
from django.contrib.auth.models import AbstractUser


class Genre(models.Model):
    style = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["style"]

    def __str__(self):
        return f"{self.style}"


class Artist(AbstractUser):
    country = models.CharField(max_length=255)
    band_name = models.CharField(max_length=255, default="Solo artist")

    class Meta:
        verbose_name = "artist"
        verbose_name_plural = "artists"

    def __str__(self):
        return f"{self.username}"


class Song(models.Model):
    song = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, related_name="songs")
    youtube_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.song
