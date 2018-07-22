"""recommendation/urls

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from django.conf.urls import include, url
from rest_framework import routers
from recommendation.views import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'episodes', EpisodeViewSet)
router.register(r'historylist-movie', HistorylistMovieViewSet)
router.register(r'historylist-show', HistorylistShowViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'shows', ShowViewSet)
router.register(r'trakt/session', TraktSessionViewSet)
router.register(r'users', UserViewSet)
router.register(r'watchlist-movie', WatchlistMovieViewSet)
router.register(r'watchlist-show', WatchlistShowViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browse-able API.
urlpatterns = [
    url(r'', include(router.urls)),
]
