from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import Women

# Create your views here.
menu = ['About', 'Add post', 'Contacts', 'Log in']


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'menu' : menu, 'title' : 'Main', 'posts' : posts})

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")