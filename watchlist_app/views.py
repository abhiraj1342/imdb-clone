from django.shortcuts import render
# here we import Movie class from model.py of watchlist_app manually
from watchlist_app.models import Movie
# here we import JsonResponse class from django.http
from django.http import JsonResponse

# Create your views here.
# we  created fuction based view only for demo purpose later we can change accordingly to our requirements 
#------------------------------------------------------------------------------------------------------------------
def movie_list(request):
    movies=Movie.objects.all() 
    #print(movies) || print(movie.values())
    data={'movies': list(movies.values())}
    return JsonResponse(data)
def movie_details(request,pk):
    movies=Movie.objects.get(pk=pk)
    data={'movies': movies.name,
          'description': movies.description,
         'active': movies.active
         }
    return JsonResponse(data)
#----------------------------------------------------------------------------------------------------------------------