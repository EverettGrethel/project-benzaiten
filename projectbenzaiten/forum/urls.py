from django.urls import path

from .views import (
community,
CommunityListView
)

urlpatterns = [
    path('', CommunityListView.as_view(), name='forum-index'),
    path('forum/<int:pk>', community.as_view(), name='forum-home')
    
]