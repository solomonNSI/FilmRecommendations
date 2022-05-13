from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.template import loader
from .models import Movies
from django.shortcuts import render
from django.http import HttpResponse

from .recommender import RecommenderEngine

import array as arr

def results(request, movie):
    try:
        finalString = movie.split("+")
        movieFirstID = []

        for i in range(3):
            temp = []
            for n in Movies.objects.filter(original_title = finalString[i]):
                temp.append(n)

            for x in temp:
                if x.original_title == finalString[i]:
                    movieFirstID.append(x.index)

        recommender = RecommenderEngine("/Users/suleymanhanyyev/github/datascience/tp6/FilmRecommendations/similarity.npy")
        results = recommender.recommend(movieFirstID)
        temp = []
        for i in results:
            for no in Movies.objects.filter(index = i):
                temp.append(no)

        context = {'listOfMovies': temp}
        return render(request, 'recommended/results.html', context)
    except Movies.DoesNotExist:
        raise Http404("Question does not exist")


def index(request):
    listOfMovies = Movies.objects.all()
    context = {'listOfMovies': listOfMovies}

    return render(request, 'recommended/index.html', context)

#     try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#       raise Http404("Question does not exist")
