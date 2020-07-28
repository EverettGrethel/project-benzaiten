from django.urls import path

from .views import (
CommunityView,
CommunityListView,
)

urlpatterns = [
    path('', CommunityListView.as_view(), name='forum-index'),
    path('forum/<int:id>', CommunityView.as_view(), name='forum-home')
    
]