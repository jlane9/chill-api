from django.test import TestCase
from recommendation.models import *


# Create your tests here.


class TraktSessionTestCase(TestCase):
    def setUp(self):
        self.session = TraktSession.objects.create(
            token="5352aebb0a98b312694a5e400e581dc3bcbfee4dee1656b7e3c00dd17aa632e8", user_slug='jrgoodle')
        self.session.get_watchlist_movies()

    def test_get_watchlist_movies_movie(self):
        self.assertEqual(Movie.objects.count(), 127)

    def test_get_watchlist_movies(self):
        self.assertEqual(WatchlistMovie.objects.count(), 127)

    def test_get_watchlist_duplicates(self):
        self.session.get_watchlist_movies()

        self.assertEqual(WatchlistMovie.objects.count(), 127)
        self.assertEqual(Movie.objects.count(), 127)
