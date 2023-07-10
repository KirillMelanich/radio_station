from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Song, Artist, Genre


class ArtistCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Artist
        fields = UserCreationForm.Meta.fields + ('artist_name', "country", "username")


class SongForm(forms.ModelForm):
    artists = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Song
        fields = "__all__"


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = "__all__"


class SongSearchForm(forms.Form):
    song = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by song name..."})
    )


class ArtistSearchForm(forms.Form):
    artist_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by artist..."})
    )
