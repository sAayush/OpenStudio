from django.urls import path
from .views import PostListCreateView, PostDetailView, RepositoryCreateView, DirectoryCreateView, FileCreateView

urlpatterns = [
    path('post/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('post/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/posts/<int:post_pk>/repository/', RepositoryCreateView.as_view(), name='repository-create'),
    path('post/repositories/<int:repository_pk>/directory/', DirectoryCreateView.as_view(), name='directory-create'),
    path('post/directories/<int:directory_pk>/file/', FileCreateView.as_view(), name='file-create'),
]