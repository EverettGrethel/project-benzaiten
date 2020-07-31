from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView)

from .models import Post, Community

class CommunityListView(ListView):
    model = Community
    template_name = 'forum/index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'communities'

class CommunityView(View):
    def get(self, request, *args, **kwargs):
        community = get_object_or_404(Community, title=kwargs['title'])
        posts = community.post_set.all()
        context = {
            'community': community,
            'posts': posts
        }
        return render(request, 'forum/home.html', context)

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        community = get_object_or_404(Community, title=kwargs['title'])
        context = {
            'community': community,
            'post': post
        }
        return render(request, 'forum/post_detail.html', context)


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView( UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView( UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

