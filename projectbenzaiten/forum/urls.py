from django.urls import path

from .views import (
CommunityView,
CommunityListView,
PostDetailView,
PostCreateView,
PostUpdateView,
PostDeleteView,
)

urlpatterns = [
    path('', CommunityListView.as_view(), name='forum-index'),
    path('forum/<str:title>/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('forum/<str:title>', CommunityView.as_view(), name='forum-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete')
]