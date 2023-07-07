from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Song, Artist, Genre


@admin.register(Artist)
class ArtistAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("country", "band_name")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("country", "band_name")}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "band_name",
                        "country",
                        "email"
                    )
                },
            ),
        )
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    search_fields = ("song",)
    list_filter = ("artists", "genre")


admin.site.register(Genre)

