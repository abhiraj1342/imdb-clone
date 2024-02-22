
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #here we added watchlist_app application urls.py manuaally 
    
      # note--we will deleted the urls.py file of watchlist_app the we have to comment its path urls  
    #path('movie/',include('watchlist_app.urls')),
    
    # we added urls.py of api folder of watchlist_app because we created new folder(named as api) in watchlist_app 
    # and want to utilize files of api folder in this project 
    # note--we will deleted the urls.py file of watchlist_app
     path('movie/',include('watchlist_app.api.urls')),
]
