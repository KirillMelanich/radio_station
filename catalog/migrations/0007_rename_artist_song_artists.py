# Generated by Django 4.2.3 on 2023-07-07 16:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0006_song_youtube_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="song",
            old_name="artist",
            new_name="artists",
        ),
    ]