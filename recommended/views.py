from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.template import loader
from .models import Movie
from django.shortcuts import render
from django.http import HttpResponse

from .recommender import RecommenderEngine

def results(request, movie):
    try:
        temp = Movie.objects.get(movie_name=movie)
        recommender = RecommenderEngine()

        return HttpResponse("You're looking at the recommendation of movies for you %s. and also \n " % temp + " " + recommender.recommend(movie))
    except Movie.DoesNotExist:
        raise Http404("Question does not exist")


def index(request):
    listOfMovies = Movie.objects.all()
    context = {'listOfMovies': listOfMovies}

    return render(request, 'recommended/index.html', context)

#     try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#       raise Http404("Question does not exist")
