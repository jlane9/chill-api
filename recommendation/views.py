"""recommendation/views

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from django.contrib.auth.models import User
from rest_framework import viewsets
from recommendation.models import Movie, WatchlistMovie
from recommendation.serializers import MovieSerializer, WatchlistMovieSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User view set instance
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Movie view set instance
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class WatchlistMovieViewSet(viewsets.ModelViewSet):
    """Watchlist movie view set instance
    """
    queryset = WatchlistMovie.objects.all()
    serializer_class = WatchlistMovieSerializer
