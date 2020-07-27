from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Post, Community

class CommunityListView(ListView):
    model = Community
    template_name = 'forum/index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'communities'

class CommunityView(View):
    def get(self, request):
        context = {
            'community': Community,
            'posts': Post.objects.all()
        }
        return render(request, 'blog/home.html', context)