from django.db import models
from datetime import datetime
from uuid import uuid4
from jsonfield import JSONField


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


class WatchlistMovie(models.Model):
    """A movie that the user wants to watch instance
    """

    id = models.UUIDField(primary_key=True, default=uuid4())
    rank = models.IntegerField(blank=False, null=False)
    type = models.CharField(default="movie", max_length=64, blank=False, null=False)
    listed_at = models.DateTimeField(default=datetime.now(), null=False)
    movie = models.ForeignKey(Movie, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Movie watched')

    def __str__(self):
        return "{movie} ({rank})".format(movie=self.movie.title, rank=self.rank)
