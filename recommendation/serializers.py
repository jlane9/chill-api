"""recommendation/serializers

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from django.contrib.auth.models import User
from rest_framework import serializers
from recommendation.models import Movie, Show, Episode, WatchlistMovie, WatchlistShow, HistorylistMovie, HistorylistShow


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer instance
    """

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Movie serializer instance
    """

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'ids', 'trakt_id', 'slug', 'imdb_id', 'tmdb_id')


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    """Show serializer instance
    """

    class Meta:
        model = Show
        fields = ('id', 'title', 'year', 'ids', 'trakt_id', 'slug', 'imdb_id', 'tvdb_id', 'tmdb_id', 'tvrage')


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    """Episode serializer instance
    """

    class Meta:
        model = Episode
        fields = ('id', 'season', 'number', 'title', 'ids', 'trakt_id', 'tvdb_id', 'imdb_id', 'tmdb_id', 'tvrage')


class WatchlistMovieSerializer(serializers.ModelSerializer):
    """Watchlist movie serializer instance
    """

    movie = MovieSerializer()

    class Meta:
        model = WatchlistMovie
        fields = ('id', 'rank', 'type', 'listed_at', 'movie')


class WatchlistShowSerializer(serializers.ModelSerializer):
    """Watchlist show serializer instance
    """

    show = ShowSerializer()

    class Meta:
        model = WatchlistShow
        fields = ('id', 'rank', 'type', 'listed_at', 'show')


class HistorylistMovieSerializer(serializers.ModelSerializer):
    """Historylist movie serializer instance
    """

    movie = MovieSerializer()

    class Meta:
        model = HistorylistMovie
        fields = ('id', 'watch_id', 'watched_at', 'action', 'type', 'movie')


class HistorylistShowSerializer(serializers.ModelSerializer):
    """Historylist show serializer instance
    """

    show = ShowSerializer()
    episode = EpisodeSerializer()

    class Meta:
        model = HistorylistMovie
        fields = ('id', 'watch_id', 'watched_at', 'action', 'type', 'episode', 'show')
