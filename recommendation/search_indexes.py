"""recommendation/search_indexes

.. codeauthor:: John Lane <john.lane93@gmail.com>
.. codeauthor:: Daniel Scharf <dscharf@fanthreesixty.com>

"""

from haystack import indexes
from recommendation.models import *


class EpisodeIndex(indexes.SearchIndex, indexes.Indexable):
    """An episode index instance
    """

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    season = indexes.IntegerField(model_attr="season")
    number = indexes.IntegerField(model_attr="number")
    title = indexes.CharField(model_attr="title")
    trakt_id = indexes.IntegerField(model_attr="trakt_id")
    tvdb_id = indexes.IntegerField(model_attr="tvdb_id")
    imdb_id = indexes.CharField(model_attr="imdb_id")
    tmdb_id = indexes.IntegerField(model_attr="tmdb_id")
    tvrage_id = indexes.IntegerField(model_attr="tvrage_id")

    def get_model(self):
        return Episode

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class HistorylistMovieIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    watch_id = indexes.CharField(model_attr='watch_id')
    watched_at = indexes.DateTimeField(model_attr='watched_at')
    action = indexes.CharField(model_attr='action')
    type = indexes.CharField(model_attr='type')
    movie_title = indexes.CharField(model_attr="movie__title")
    movie_year = indexes.CharField(model_attr="movie__year")
    movie_ids_trakt = indexes.IntegerField(model_attr="movie__trakt_id")
    movie_ids_slug = indexes.CharField(model_attr="movie__slug")
    movie_ids_imdb = indexes.CharField(model_attr="movie__imdb_id")
    movie_ids_tmdb = indexes.IntegerField(model_attr="movie__tmdb_id")

    def get_model(self):
        return HistorylistMovie

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class HistorylistShowIndex(indexes.SearchIndex, indexes.Indexable):
    """A history list show index instance
    """

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    watch_id = indexes.CharField(model_attr='watch_id')
    watched_at = indexes.DateTimeField(model_attr='watched_at')
    action = indexes.CharField(model_attr='action')
    type = indexes.CharField(model_attr='type')
    show_title = indexes.CharField(model_attr="show__title")
    show_year = indexes.CharField(model_attr="show__year")
    show_ids_trakt = indexes.IntegerField(model_attr="show__trakt_id")
    show_ids_slug = indexes.CharField(model_attr="show__slug")
    show_ids_imdb = indexes.CharField(model_attr="show__imdb_id")
    show_ids_tmdb = indexes.IntegerField(model_attr="show__tmdb_id")

    def get_model(self):
        return HistorylistShow

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    """A movie index instance
    """

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    title = indexes.CharField(model_attr="title")
    year = indexes.CharField(model_attr="year")
    trakt_id = indexes.IntegerField(model_attr="trakt_id")
    slug = indexes.CharField(model_attr="slug")
    imdb_id = indexes.CharField(model_attr="imdb_id")
    tmdb_id = indexes.IntegerField(model_attr="tmdb_id")

    def get_model(self):
        return Movie

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class ShowIndex(indexes.SearchIndex, indexes.Indexable):
    """A show index instance
    """

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    title = indexes.CharField(model_attr="title")
    year = indexes.CharField(model_attr="year")
    trakt_id = indexes.IntegerField(model_attr="trakt_id")
    slug = indexes.CharField(model_attr="slug")
    tvdb_id = indexes.IntegerField(model_attr="tvdb_id")
    imdb_id = indexes.CharField(model_attr="imdb_id")
    tmdb_id = indexes.IntegerField(model_attr="tmdb_id")
    tvrage_id = indexes.IntegerField(model_attr="tvrage_id")

    def get_model(self):
        return Show

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class WatchlistMovieIndex(indexes.SearchIndex, indexes.Indexable):
    """A watchlist movie index instance
    """

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    rank = indexes.IntegerField(model_attr='rank')
    type = indexes.CharField(model_attr='type')
    listed_at = indexes.DateTimeField(model_attr='listed_at')
    movie_title = indexes.CharField(model_attr="movie__title")
    movie_year = indexes.CharField(model_attr="movie__year")
    movie_ids_trakt = indexes.IntegerField(model_attr="movie__trakt_id")
    movie_ids_slug = indexes.CharField(model_attr="movie__slug")
    movie_ids_imdb = indexes.CharField(model_attr="movie__imdb_id")
    movie_ids_tmdb = indexes.IntegerField(model_attr="movie__tmdb_id")

    def get_model(self):
        return WatchlistMovie

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class WatchlistShowIndex(indexes.SearchIndex, indexes.Indexable):
    """A watchlist show index instance
    """

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    rank = indexes.IntegerField(model_attr='rank')
    type = indexes.CharField(model_attr='type')
    listed_at = indexes.DateTimeField(model_attr='listed_at')
    show_title = indexes.CharField(model_attr="show__title")
    show_year = indexes.CharField(model_attr="show__year")
    show_ids_trakt = indexes.IntegerField(model_attr="show__trakt_id")
    show_ids_slug = indexes.CharField(model_attr="show__slug")
    show_ids_tvdb = indexes.IntegerField(model_attr="show__tvdb_id")
    show_ids_imdb = indexes.CharField(model_attr="show__imdb_id")
    show_ids_tmdb = indexes.IntegerField(model_attr="show__tmdb_id")
    show_ids_tvrage = indexes.IntegerField(model_attr="show__tvrage_id")

    def get_model(self):
        return WatchlistShow

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
