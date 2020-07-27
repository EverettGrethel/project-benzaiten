from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Community

class CommunityListView(ListView):
    model = Community
    template_name = 'forum/index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'communities'

def community(request):
    context = {

        'posts': Post.objects.filter(community=)
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'forum/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5