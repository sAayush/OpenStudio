from rest_framework import serializers
from .models import Post, Tag, Repository, Directory, File

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'tags', 'photo', 'has_code', 'created_at', 'updated_at']

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=50))

    class Meta:
        model = Post
        fields = ['title', 'description', 'tags', 'photo', 'has_code']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.has_code = validated_data.get('has_code', instance.has_code)
        instance.save()

        instance.tags.clear()
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        
        return instance

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'content']

class DirectorySerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)
    subdirectories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Directory
        fields = ['id', 'name', 'files', 'subdirectories']

class RepositorySerializer(serializers.ModelSerializer):
    directories = DirectorySerializer(many=True, read_only=True)

    class Meta:
        model = Repository
        fields = ['id', 'directories']
