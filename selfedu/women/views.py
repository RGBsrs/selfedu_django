from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Women
from .forms import AddPostForm


# Create your views here.
menu = [
    {'title': "О сайте", 'url_name' : 'about'},
    {'title': "Добавить статью", 'url_name' : 'add_page'},
    {'title': "Обратная связь", 'url_name' : 'contact'},
    {'title': "Вход", 'url_name' : 'login'},
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts' : posts,
        'menu' : menu, 
        'title' : "Главная страница", 
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context = context)

def about(request):
    return render(request, 'women/about.html')

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'title': 'Добавление статьи', 'menu': menu})

def contact(request):
    return HttpResponse("Contacts")

def login(request):
    return HttpResponse("logged in")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug = post_slug)

    context = {
        'post' : post,
        'menu' : menu, 
        'title' : post.title, 
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context= context)


def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug = cat_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts' : posts,
        'menu' : menu, 
        'title' : "Отображение по рубрикам", 
        'cat_selected': posts.first().cat_id,
    }
    return render(request, 'women/index.html', context = context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")