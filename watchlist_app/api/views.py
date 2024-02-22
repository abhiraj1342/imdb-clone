# import model class of model.py in views.py
from watchlist_app.models import Movie

#we have to import api_view decorator here bcz we are created function based views so we have tell that
# which type of request we are interested in.
from rest_framework.decorators import api_view

#import serialzers class
from watchlist_app.api.serializers import MovieSerializer

#import response from drf
from rest_framework.response import Response


# we created function for viewS

#we have to tell which type of request we are performing by using the decorator(@api_view)
@api_view()#by default it is GET type
def movie_list(request):
    movies=Movie.objects.all() # it is complex data 
    serializer=MovieSerializer(movies,many=True) #we converting complex data into python native objects
    return Response(serializer.data) # we return json format of python native objects

@api_view()
def movie_details(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)