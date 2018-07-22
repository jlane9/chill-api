"""recommendation/models

.. codeauthor:: John Lane <john.lane93@gmail.com>
.. codeauthor:: Daniel Scharf <dscharf@fanthreesixty.com>

"""

from uuid import uuid4
from django.db import models
from django.conf import settings
from django.utils.timezone import now
from requests import request

__all__ = ['Movie', 'Show', 'Episode', 'HistorylistMovie', 'HistorylistShow', 'MovieRecommendation', 'WatchlistMovie',
           'WatchlistShow', 'TraktSession']


class Movie(models.Model):
    """A movie instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=1024)
    year = models.IntegerField(null=False, blank=False)
    trakt_id = models.IntegerField(null=False, blank=False, default=-1)
    slug = models.CharField(null=False, blank=False, max_length=1024)
    imdb_id = models.CharField(null=False, blank=False, max_length=256)
    tmdb_id = models.IntegerField(null=False, blank=False, default=-1)

    def __str__(self):
        return "{title} ({year})".format(title=self.title, year=self.year)


class Show(models.Model):
    """A show instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=1024)
    year = models.IntegerField(null=False, blank=False)
    trakt_id = models.IntegerField(null=False, blank=False, default=-1)
    slug = models.CharField(null=False, blank=False, max_length=1024)
    imdb_id = models.CharField(null=False, blank=False, max_length=256)
    tvdb_id = models.IntegerField(null=False, blank=False, default=-1)
    tvrage_id = models.IntegerField(null=False, blank=False, default=-1)

    def __str__(self):
        return "{title} ({year})".format(title=self.title, year=self.year)


class Episode(models.Model):
    """An episode instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    season = models.IntegerField(null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=1024)
    trakt_id = models.IntegerField(null=False, blank=False, default=-1)
    slug = models.CharField(null=False, blank=False, max_length=1024)
    imdb_id = models.CharField(null=False, blank=False, max_length=256)
    tvdb_id = models.IntegerField(null=False, blank=False, default=-1)
    tvrage_id = models.IntegerField(null=False, blank=False, default=-1)

    def __str__(self):
        return "{title} (S:{season}E:{episode})".format(title=self.title, season=self.season, episode=self.number)


class HistorylistMovie(models.Model):
    """A movie that the user has already watched instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    watch_id = models.IntegerField(blank=False, null=False)
    watched_at = models.DateTimeField(default=now, null=False)
    action = models.CharField(default="watch", max_length=64, blank=False, null=False)
    type = models.CharField(default="movie", max_length=64, blank=False, null=False)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Movie watched')
    user_slug = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return "{movie} ({watched})".format(movie=self.movie.title, watched=self.watched_at)


class HistorylistShow(models.Model):
    """A show that the user has already watched instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    watch_id = models.IntegerField(blank=False, null=False)
    watched_at = models.DateTimeField(default=now, null=False)
    action = models.CharField(default="watch", max_length=64, blank=False, null=False)
    type = models.CharField(default="show", max_length=64, blank=False, null=False)
    episode = models.ForeignKey(Episode, blank=False, null=False, on_delete=models.CASCADE,
                                verbose_name='Episode watched')
    show = models.ForeignKey(Show, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Show watched')
    user_slug = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return "{show} ({watched})".format(show=self.show.title, watched=self.watched_at)


class MovieRecommendation(object):

    def __init__(self, **kwargs):
        for field in ('movie_id', 'movie_title', 'movie_year', 'movie_trakt_id', 'movie_slug', 'movie_imdb_id',
                      'movie_tmdb_id'):
            setattr(self, field, kwargs.get(field, None))


class ShowRecommendation(object):

    def __init__(self, **kwargs):
        for field in ('show_id', 'show_title', 'show_year', 'show_trakt_id', 'show_slug', 'show_imdb_id',
                      'show_tmdb_id'):
            setattr(self, field, kwargs.get(field, None))


class WatchlistMovie(models.Model):
    """A movie that the user wants to watch instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    rank = models.IntegerField(blank=False, null=False)
    type = models.CharField(default="movie", max_length=64, blank=False, null=False)
    listed_at = models.DateTimeField(default=now, null=False)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Movie watched')
    user_slug = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return "{movie} ({rank})".format(movie=self.movie.title, rank=self.rank)


class WatchlistShow(models.Model):
    """A show that the user wants to watch instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    rank = models.IntegerField(blank=False, null=False)
    type = models.CharField(default="show", max_length=64, blank=False, null=False)
    listed_at = models.DateTimeField(default=now, null=False)
    show = models.ForeignKey(Show, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Show watched')
    user_slug = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return "{show} ({rank})".format(show=self.show.title, rank=self.rank)


class TraktSession(models.Model):
    """A trakt session instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4)
    user_slug = models.CharField(max_length=1024, null=False, blank=False)
    token = models.CharField(max_length=128, null=False, blank=False)

    create_dt = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    update_dt = models.DateTimeField(auto_now_add=True, verbose_name="Last updated")

    def __str__(self):
        return "{user_slug} ({token})".format(user_slug=self.user_slug, token=self.token)

    def get_watchlist_movies(self):

        url = "https://api.trakt.tv/users/{user}/watchlist/movies".format(user=self.user_slug)

        headers = {
            'Content-type': "application/json",
            'trakt-api-key': settings.API_KEY,
            'trakt-api-version': "2",
            'Authorization': "Bearer {token}".format(token=self.token)
        }

        response = request("GET", url, headers=headers)

        if response.ok:
            watch_list = response.json()

            for item in watch_list:

                movie = Movie.objects.filter(trakt_id=item["movie"]["ids"]["trakt"]).first()

                if movie:
                    pass

                else:
                    data = {
                        "title": item["movie"].get("title"),
                        "year": item["movie"].get("year"),
                        "trakt_id": item["movie"]["ids"].get("trakt", -1),
                        "slug": item["movie"]["ids"].get("slug", ""),
                        "imdb_id": item["movie"]["ids"].get("imdb", ""),
                        "tmdb_id": item["movie"]["ids"].get("tmdb", -1)
                    }
                    movie = Movie.objects.create(**data)
                    movie.save()

                watch_list_item = WatchlistMovie.objects.filter(user_slug=self.user_slug,
                                                                movie__trakt_id=item["movie"]["ids"]["trakt"]).first()

                if watch_list_item:
                    watch_list_item.rank = item.get("rank", -1)
                    watch_list_item.type = item.get("type", "movie")

                else:

                    data = {
                        "rank": item.get("rank", -1),
                        "listed_at": item.get("listed_at", now()),
                        "type": item.get("type", "movie"),
                        "movie": movie,
                        "user_slug": self.user_slug
                    }

                    watch_list_item = WatchlistMovie.objects.create(**data)

                watch_list_item.save()

    def update_info(self):

        self.get_watchlist_movies()
