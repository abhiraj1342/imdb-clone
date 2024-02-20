
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #here we added watchlist_app application urls.py manuaally 
    path('movie/',include('watchlist_app.urls')),
]
