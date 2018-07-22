"""recommendation/urls

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from django.conf.urls import include, url
from rest_framework import routers
from recommendation.views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browse-able API.
urlpatterns = [
    url(r'', include(router.urls)),
]
