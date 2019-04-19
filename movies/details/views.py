from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Movie

def home(request):
    try:
        movies = Movie.objects.all()
    except Movie.DoesNotExist:
        raise Http404('No movie found')
    return render(request, 'home.html', {'movies': movies})

def mdetail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404('Movie not found')
    return render(request, 'mdetail.html', {'movie': movie})