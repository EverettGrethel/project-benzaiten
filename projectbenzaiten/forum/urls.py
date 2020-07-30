from django.urls import path

from .views import (
CommunityView,
CommunityListView,
PostDetailView
)

urlpatterns = [
    path('', CommunityListView.as_view(), name='forum-index'),
    path('forum/<str:title>/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('forum/<str:title>', CommunityView.as_view(), name='forum-home')
]