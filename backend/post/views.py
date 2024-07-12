from rest_framework import generics, permissions
from .models import Post, Repository, Directory, File
from .serializers import PostSerializer, PostCreateUpdateSerializer, RepositorySerializer, DirectorySerializer, FileSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateUpdateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostCreateUpdateSerializer
        return PostSerializer

class RepositoryCreateView(generics.CreateAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(post=post)

class DirectoryCreateView(generics.CreateAPIView):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        repository = Repository.objects.get(pk=self.kwargs['repository_pk'])
        parent_directory = Directory.objects.get(pk=self.kwargs.get('parent_pk', None))
        serializer.save(repository=repository, parent=parent_directory)

class FileCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        directory = Directory.objects.get(pk=self.kwargs['directory_pk'])
        serializer.save(directory=directory)
