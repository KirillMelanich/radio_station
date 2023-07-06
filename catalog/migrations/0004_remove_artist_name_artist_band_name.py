# Generated by Django 4.2.3 on 2023-07-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_artist_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artist",
            name="name",
        ),
        migrations.AddField(
            model_name="artist",
            name="band_name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
