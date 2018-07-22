"""recommendation/admin

.. codeauthor:: John Lane <john.lane93@me.com>
.. codeauthor:: Daniel Scharf <dscharf@fanthreesixty.com>

"""

from django.contrib import admin
from recommendation.models import *

admin.site.register(Episode)
admin.site.register(HistorylistMovie)
admin.site.register(HistorylistShow)
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(TraktSession)
admin.site.register(WatchlistMovie)
admin.site.register(WatchlistShow)

