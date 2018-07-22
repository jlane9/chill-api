"""recommendation/views

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from django.contrib.auth.models import User
from rest_framework import viewsets
from recommendation.models import Movie, Show, Episode, WatchlistMovie, WatchlistShow, HistorylistMovie, HistorylistShow
from recommendation.serializers import MovieSerializer, ShowSerializer, EpisodeSerializer, WatchlistMovieSerializer, \
    WatchlistShowSerializer, HistorylistMovieSerializer, HistorylistShowSerializer, UserSerializer


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


class ShowViewSet(viewsets.ModelViewSet):
    """Show view set instance
    """

    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    """Episode view set instance
    """

    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


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


class HistorylistMovieViewSet(viewsets.ModelViewSet):
    """Historylist movie view set instance
    """
    queryset = HistorylistMovie.objects.all()
    serializer_class = HistorylistMovieSerializer


class HistorylistShowViewSet(viewsets.ModelViewSet):
    """Historylist show view set instance
    """
    queryset = HistorylistShow.objects.all()
    serializer_class = HistorylistShowSerializer
