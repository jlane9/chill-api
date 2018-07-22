"""recommendation/serializers

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from django.contrib.auth.models import User
from rest_framework import serializers
from recommendation.models import Movie, WatchlistMovie


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


class WatchlistMovieSerializer(serializers.ModelSerializer):
    """Watchlist movie serializer instance
    """

    movie = MovieSerializer()

    class Meta:
        model = WatchlistMovie
        fields = ('id', 'rank', 'type', 'listed_at', 'movie')
