from django.contrib import admin
#here we import Movie class from models.py of watchlist_app 
from watchlist_app.models import Movie
# Register your models here.
#here we register our Movie class model without registering its will not refect to admin panel
admin.site.register(Movie)
