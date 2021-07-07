from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    return HttpResponse("Hello")

def archive(request, year):
    if year > 2020:
        return redirect('home', permanent=False)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")