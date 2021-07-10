from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    return render(request, 'women/index.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")