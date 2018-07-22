from django.test import TestCase
from recommendation.models import *


# Create your tests here.


class TraktSessionTestCase(TestCase):
    def setUp(self):
        self.session = TraktSession.objects.create(
            token="5352aebb0a98b312694a5e400e581dc3bcbfee4dee1656b7e3c00dd17aa632e8", user_slug='jrgoodle')
        self.session.get_watchlist_movies()
        self.session.get_watchlist_shows()
        self.session.get_historylist_movies()

    # Watchlist movies
    def test_get_watchlist_movies_movie(self):
        self.assertEqual(Movie.objects.count(), 137)

    def test_get_watchlist_movies(self):
        self.assertEqual(WatchlistMovie.objects.count(), 127)

    def test_get_watchlist_movies_duplicates(self):
        self.session.get_watchlist_movies()

        self.assertEqual(WatchlistMovie.objects.count(), 127)
        self.assertEqual(Movie.objects.count(), 137)

    # Watchlist shows
    def test_get_watchlist_shows_show(self):
        self.assertEqual(Show.objects.count(), 10)

    def test_get_watchlist_shows(self):
        self.assertEqual(WatchlistShow.objects.count(), 10)

    def test_get_watchlist_shows_duplicates(self):
        self.session.get_watchlist_shows()

        self.assertEqual(WatchlistShow.objects.count(), 10)
        self.assertEqual(Show.objects.count(), 10)

    # History movies
    def test_get_historylist_movies(self):
        self.assertEqual(HistorylistMovie.objects.count(), 10)

    def test_get_historylist_movies_duplicates(self):
        self.session.get_historylist_movies()
        self.assertEqual(HistorylistMovie.objects.count(), 10)

    # History shows
    def test_get_historylist_shows(self):
        self.assertEqual(HistorylistShow.objects.count(), 10)

    def test_get_historylist_shows_duplicates(self):
        self.session.get_historylist_shows()
        self.assertEqual(HistorylistShow.objects.count(), 10)
