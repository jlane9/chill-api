"""recommendation/models

.. codeauthor:: John Lane <john.lane93@gmail.com>
.. codeauthor:: Daniel Scharf <dscharf@fanthreesixty.com>

"""

from django.db import models
from django.utils.timezone import now
from uuid import uuid4
from jsonfield import JSONField

__all__ = ['Movie', 'Show', 'Episode', 'HistorylistMovie', 'HistorylistShow', 'WatchlistMovie', 'WatchlistShow',
           'TraktSession']


class Movie(models.Model):
    """A movie instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    title = models.CharField(max_length=1024)
    year = models.IntegerField(null=False, blank=False)
    ids = JSONField(blank=True, null=True)

    @property
    def trakt_id(self):
        return self.ids["trakt"] if "trakt" in self.ids else -1

    @property
    def slug(self):
        return self.ids["slug"] if "slug" in self.ids else ''

    @property
    def imdb_id(self):
        return self.ids["imdb"] if "imdb" in self.ids else ''

    @property
    def tmdb_id(self):
        return self.ids["tmdb"] if "tmdb" in self.ids else -1

    def __str__(self):
        return "{title} ({year})".format(title=self.title, year=self.year)


class Show(models.Model):
    """A show instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    title = models.CharField(max_length=1024)
    year = models.IntegerField(null=False, blank=False)
    ids = JSONField(blank=True, null=True)

    @property
    def trakt_id(self):
        return self.ids["trakt"] if "trakt" in self.ids else -1

    @property
    def slug(self):
        return self.ids["slug"] if "slug" in self.ids else ''

    @property
    def imdb_id(self):
        return self.ids["imdb"] if "imdb" in self.ids else ''

    @property
    def tvdb_id(self):
        return self.ids["tvdb"] if "tvdb" in self.ids else -1

    @property
    def tmdb_id(self):
        return self.ids["tmdb"] if "tmdb" in self.ids else -1

    @property
    def tvrage(self):
        return self.ids["tvrage"] if "tvrage" in self.ids else -1

    def __str__(self):
        return "{title} ({year})".format(title=self.title, year=self.year)


class Episode(models.Model):
    """An episode instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    season = models.IntegerField(null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=1024)
    ids = JSONField(blank=True, null=True)

    @property
    def trakt_id(self):
        return self.ids["trakt"] if "trakt" in self.ids else -1

    @property
    def tvdb_id(self):
        return self.ids["tvdb"] if "tvdb" in self.ids else -1

    @property
    def imdb_id(self):
        return self.ids["imdb"] if "imdb" in self.ids else ''

    @property
    def tmdb_id(self):
        return self.ids["tmdb"] if "tmdb" in self.ids else -1

    @property
    def tvrage(self):
        return self.ids["tmdb"] if "tmdb" in self.ids else -1

    def __str__(self):
        return "{title} (S:{season}E:{episode})".format(title=self.title, season=self.season, episode=self.episode)


class HistorylistMovie(models.Model):
    """A movie that the user has already watched instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    watch_id = models.IntegerField(blank=False, null=False)
    watched_at = models.DateTimeField(default=now, null=False)
    action = models.CharField(default="watch", max_length=64, blank=False, null=False)
    type = models.CharField(default="movie", max_length=64, blank=False, null=False)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Movie watched')

    def __str__(self):
        return "{movie} ({watched})".format(movie=self.movie.title, watched=self.watched_at)


class HistorylistShow(models.Model):
    """A show that the user has already watched instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    watch_id = models.IntegerField(blank=False, null=False)
    watched_at = models.DateTimeField(default=now, null=False)
    action = models.CharField(default="watch", max_length=64, blank=False, null=False)
    type = models.CharField(default="show", max_length=64, blank=False, null=False)
    episode = models.ForeignKey(Episode, blank=False, null=False, on_delete=models.CASCADE,
                                verbose_name='Episode watched')
    show = models.ForeignKey(Show, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Show watched')

    def __str__(self):
        return "{show} ({watched})".format(show=self.show.title, watched=self.watched_at)


class WatchlistMovie(models.Model):
    """A movie that the user wants to watch instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    rank = models.IntegerField(blank=False, null=False)
    type = models.CharField(default="movie", max_length=64, blank=False, null=False)
    listed_at = models.DateTimeField(default=now, null=False)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Movie watched')

    def __str__(self):
        return "{movie} ({rank})".format(movie=self.movie.title, rank=self.rank)


class WatchlistShow(models.Model):
    """A show that the user wants to watch instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    rank = models.IntegerField(blank=False, null=False)
    type = models.CharField(default="show", max_length=64, blank=False, null=False)
    listed_at = models.DateTimeField(default=now, null=False)
    show = models.ForeignKey(Show, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Show watched')

    def __str__(self):
        return "{show} ({rank})".format(show=self.show.title, rank=self.rank)


class TraktSession(models.Model):
    """A trakt session instance
    """

    user_slug = models.CharField(max_length=1024, null=False, blank=False)
    token = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return "{user_slug} ({token})".format(user_slug=self.user_slug, token=self.token)
