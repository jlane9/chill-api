from django.contrib import admin
from recommendation.models import Movie, WatchlistMovie

# Register your models here.

admin.site.register(Movie)
admin.site.register(WatchlistMovie)
