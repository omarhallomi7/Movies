# movies/admin.py
from django.contrib import admin
from .models import Movie,Review

# Movie registeration in admin
admin.site.register(Movie)

# Review registeration in admin
admin.site.register(Review)