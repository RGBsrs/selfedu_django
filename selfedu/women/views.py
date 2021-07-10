from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import Category, Women

# Create your views here.
menu = [
    {'title': "О сайте", 'url_name' : 'about'},
    {'title': "Добавить статью", 'url_name' : 'add_page'},
    {'title': "Обратная связь", 'url_name' : 'contact'},
    {'title': "Вход", 'url_name' : 'login'},
]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts' : posts,
        'cats' : cats,
        'menu' : menu, 
        'title' : "Главная страница", 
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context = context)

def about(request):
    return render(request, 'women/about.html')

def addpage(request):
    return HttpResponse("Post added")

def contact(request):
    return HttpResponse("Contacts")

def login(request):
    return HttpResponse("logged in")

def show_post(request, post_id):
    return HttpResponse(f"Post with pk - {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id = cat_id)
    cats = Category.objects.all()
    context = {
        'posts' : posts,
        'cats' : cats,
        'menu' : menu, 
        'title' : "Отображение по рубрикам", 
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context = context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")