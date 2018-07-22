"""recommendation/views

.. codeauthor:: John Lane <john.lane93@gmail.com>
.. codeauthor:: Daniel Scharf <dscharf@fanthreesixty.com>

"""

from django.contrib.auth.models import User
from haystack.query import SearchQuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from recommendation.models import *
from recommendation.serializers import *

__all__ = ['EpisodeViewSet', 'HistorylistMovieViewSet', 'HistorylistShowViewSet', 'MovieViewSet', 'ShowViewSet',
           'TraktSessionViewSet', 'UserViewSet', 'WatchlistMovieViewSet',  'WatchlistShowViewSet']


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

    @action(methods=['post'], detail=False)
    def recommendation(self, request):
        """Retrieve recommendation from movies in history

        :param request:
        :return:
        """

        if request:
            pass

        queryset = SearchQuerySet().models(HistorylistMovie).all()
        serializer = HistorylistMovieSerializer(queryset, many=True)

        return Response(serializer.data)


class HistorylistShowViewSet(viewsets.ModelViewSet):
    """History list show view set instance
    """
    queryset = HistorylistShow.objects.all()
    serializer_class = HistorylistShowSerializer

    @action(methods=['post'], detail=False)
    def recommendation(self, request):
        """Retrieve recommendation from shows in history

        :param request:
        :return:
        """

        if request:
            pass

        queryset = SearchQuerySet().models(HistorylistShow).all()
        serializer = HistorylistShowSerializer(queryset, many=True)

        return Response(serializer.data)


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

    @action(methods=['post'], detail=False)
    def recommendation(self, request):
        """Retrieve recommendation from movies in watchlist

        :param request:
        :return:
        """

        if request:
            pass

        queryset = SearchQuerySet().models(WatchlistMovie).all()
        serializer = WatchlistMovieSerializer(queryset, many=True)

        return Response(serializer.data)


class WatchlistShowViewSet(viewsets.ModelViewSet):
    """Watchlist show view set instance
    """
    queryset = WatchlistShow.objects.all()
    serializer_class = WatchlistShowSerializer

    @action(methods=['post'], detail=False)
    def recommendation(self, request):
        """Retrieve recommendation from shows in watchlist

        :param request:
        :return:
        """

        if request:
            pass

        queryset = SearchQuerySet().models(WatchlistShow).all()
        serializer = WatchlistShowSerializer(queryset, many=True)

        return Response(serializer.data)
