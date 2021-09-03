from django.db import models
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .models import Category, Women
from .forms import AddPostForm


# Create your views here.
menu = [
    {'title': "О сайте", 'url_name' : 'about'},
    {'title': "Добавить статью", 'url_name' : 'add_page'},
    {'title': "Обратная связь", 'url_name' : 'contact'},
    {'title': "Вход", 'url_name' : 'login'},
]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Главная страница"
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published = True)

# def index(request):
#     posts = Women.objects.all()
#     context = {
#         'posts' : posts,
#         'menu' : menu, 
#         'title' : "Главная страница", 
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context = context)

def about(request):
    return render(request, 'women/about.html')

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
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


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")