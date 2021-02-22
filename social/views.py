from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'social/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'social/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailsView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['author', 'title', 'content']


class PostUpdateView(UpdateView):
    model = Post
    fields = ['author', 'title', 'content']


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
