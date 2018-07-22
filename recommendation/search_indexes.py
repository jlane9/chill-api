from haystack import indexes
from recommendation.models import WatchlistMovie


class WatchlistMovieIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    id = indexes.CharField(model_attr='id')
    rank = indexes.IntegerField(model_attr='rank')
    type = indexes.CharField(model_attr='type')
    listed_at = indexes.DateTimeField(model_attr='listed_at')

    def get_model(self):
        return WatchlistMovie

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
