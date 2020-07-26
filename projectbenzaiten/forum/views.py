from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'forum/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'communities'
    ordering = ['-date_posted']
    paginate_by = 5