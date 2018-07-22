"""recommendation/views

.. codeauthor:: John Lane <john.lane93@gmail.com>
.. codeauthor:: Daniel Scharf <dscharf@fanthreesixty.com>

"""

from django.contrib.auth.models import User
from rest_framework import viewsets
from recommendation.models import *
from recommendation.serializers import *

__all__ = ['EpisodeViewSet', 'HistorylistMovieViewSet', 'HistorylistShowViewSet', 'MovieViewSet', 'ShowViewSet',
           'TraktSessionViewSet', 'UserViewSet', 'WatchlistMovieViewSet', 'WatchlistShowViewSet']


class EpisodeViewSet(viewsets.ModelViewSet):
    """Episode view set instance
    """

    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class HistorylistMovieViewSet(viewsets.ModelViewSet):
    """History list movie view set instance
    """
    queryset = HistorylistMovie.objects.all()
    serializer_class = HistorylistMovieSerializer


class HistorylistShowViewSet(viewsets.ModelViewSet):
    """History list show view set instance
    """
    queryset = HistorylistShow.objects.all()
    serializer_class = HistorylistShowSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Movie view set instance
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ShowViewSet(viewsets.ModelViewSet):
    """Show view set instance
    """

    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class TraktSessionViewSet(viewsets.ModelViewSet):
    """Trakt session view set instance
    """

    queryset = TraktSession.objects.all()
    serializer_class = TraktSessionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User view set instance
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class WatchlistMovieViewSet(viewsets.ModelViewSet):
    """Watchlist movie view set instance
    """
    queryset = WatchlistMovie.objects.all()
    serializer_class = WatchlistMovieSerializer


class WatchlistShowViewSet(viewsets.ModelViewSet):
    """Watchlist show view set instance
    """
    queryset = WatchlistShow.objects.all()
    serializer_class = WatchlistShowSerializer
