# Generated by Django 4.2.3 on 2023-07-06 17:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artist",
            name="name",
        ),
    ]
