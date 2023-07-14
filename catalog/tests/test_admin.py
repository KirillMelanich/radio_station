from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.test import TestCase
from catalog.admin import ArtistAdmin, SongAdmin
from catalog.models import Artist, Song


class ArtistAdminTest(TestCase):
    def test_list_display(self):
        expected_list_display = UserAdmin.list_display + ("country", "artist_name")
        self.assertEqual(ArtistAdmin.list_display, expected_list_display)

    def test_fieldsets(self):
        expected_fieldsets = UserAdmin.fieldsets + (
            (
                "Additional info",
                {
                    "fields": ("country", "artist_name"),
                },
            ),
        )
        self.assertEqual(ArtistAdmin.fieldsets, expected_fieldsets)

    def test_registered_model(self):
        self.assertTrue(admin.site.is_registered(Artist))

    def test_correct_model_admin(self):
        self.assertIsInstance(admin.site._registry[Artist], ArtistAdmin)


class SongAdminTest(TestCase):
    def test_search_fields(self):
        expected_search_fields = ("song",)
        self.assertEqual(SongAdmin.search_fields, expected_search_fields)

    def test_list_filter(self):
        expected_list_filter = ("artists", "genre")
        self.assertEqual(SongAdmin.list_filter, expected_list_filter)

    def test_registered_model(self):
        self.assertTrue(admin.site.is_registered(Song))

    def test_correct_model_admin(self):
        self.assertIsInstance(admin.site._registry[Song], SongAdmin)
