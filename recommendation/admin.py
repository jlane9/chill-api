from django.contrib import admin
from recommendation.models import Movie, Show, Episode, WatchlistMovie, WatchlistShow, HistorylistMovie, HistorylistShow

# Register your models here.

admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(WatchlistMovie)
admin.site.register(WatchlistShow)
admin.site.register(HistorylistMovie)
admin.site.register(HistorylistShow)

