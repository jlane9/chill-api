from haystack import indexes
from recommendation.models import WatchlistMovie


class WatchlistMovieIndex(indexes.SearchIndex, indexes.Indexable):

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
