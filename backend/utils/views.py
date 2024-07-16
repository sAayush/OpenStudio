from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import CustomUser
from post.models import Post, Tag
from .serializers import UserSerializer, PostSerializer, TagSerializer

class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', None)
        if query:
            users = CustomUser.objects.filter(username__icontains=query) | CustomUser.objects.filter(email__icontains=query)
            posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(description__icontains=query)
            tags = Tag.objects.filter(name__icontains=query)

            user_serializer = UserSerializer(users, many=True)
            post_serializer = PostSerializer(posts, many=True)
            tag_serializer = TagSerializer(tags, many=True)

            return Response({
                'users': user_serializer.data,
                'posts': post_serializer.data,
                'tags': tag_serializer.data
            })
        return Response({
            'users': [],
            'posts': [],
            'tags': []
        })
