from django.db import models
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Women
from .forms import AddPostForm
from .utils import DataMixin, menu


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published = True)

def about(request):
    return render(request, 'women/about.html')

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

def contact(request):
    return HttpResponse("Contacts")

def login(request):
    return HttpResponse("logged in")

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['post'])
        return dict(list(context.items()) + list(c_def.items()))



class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                    cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")