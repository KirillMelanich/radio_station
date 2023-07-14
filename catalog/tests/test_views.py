from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from catalog.models import Genre, Artist, Song


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = Artist.objects.create_user(username='testuser', password='testpassword')

    def test_index_view_with_login(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/index.html')
        self.assertContains(response, 'Welcome to the home page')

        # Check if the context variables are passed correctly
        self.assertEqual(response.context['num_artists'], Artist.objects.count())
        self.assertEqual(response.context['num_songs'], Song.objects.count())
        self.assertEqual(response.context['num_genres'], Genre.objects.count())
        self.assertEqual(response.context['num_visits'], 1)

        # Check if the session value is incremented correctly
        self.assertEqual(self.client.session['num_visits'], 1)

    def test_index_view_without_login(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/')