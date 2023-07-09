from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Song, Artist


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
