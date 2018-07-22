"""recommendation/serializers

.. codeauthor:: John Lane <john.lane93@gmail.com>
.. codeauthor:: Daniel Scharf <dscharf@fanthreesixty.com>

"""

from django.contrib.auth.models import User
from rest_framework import serializers
from recommendation.models import *

__all__ = ['EpisodeSerializer', 'MovieSerializer', 'ShowSerializer', 'HistorylistMovieSerializer',
           'HistorylistShowSerializer', 'TraktSessionSerializer', 'UserSerializer', 'WatchlistMovieSerializer',
           'WatchlistShowSerializer']


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    """Episode serializer instance
    """

    class Meta:
        model = Episode
        fields = ('id', 'season', 'number', 'title', 'trakt_id', 'tvdb_id', 'imdb_id', 'tmdb_id', 'tvrage')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Movie serializer instance
    """

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'trakt_id', 'slug', 'imdb_id', 'tmdb_id')


class ShowSerializer(serializers.HyperlinkedModelSerializer):
    """Show serializer instance
    """

    class Meta:
        model = Show
        fields = ('id', 'title', 'year', 'trakt_id', 'slug', 'imdb_id', 'tvdb_id', 'tmdb_id', 'tvrage')


class HistorylistMovieSerializer(serializers.ModelSerializer):
    """History list movie serializer instance
    """

    movie = MovieSerializer()

    class Meta:
        model = HistorylistMovie
        fields = ('id', 'watch_id', 'watched_at', 'action', 'type', 'movie')


class HistorylistShowSerializer(serializers.ModelSerializer):
    """History list show serializer instance
    """

    show = ShowSerializer()
    episode = EpisodeSerializer()

    class Meta:
        model = HistorylistShow
        fields = ('id', 'watch_id', 'watched_at', 'action', 'type', 'episode', 'show')


class TraktSessionSerializer(serializers.ModelSerializer):
    """Trakt session serializer instance
    """

    class Meta:
        model = TraktSession
        fields = ('user_slug', 'token')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer instance
    """

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


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
