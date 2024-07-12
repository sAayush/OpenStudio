import os
from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    photo = models.ImageField(upload_to='post_photos/')
    has_code = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Repository(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='repository')

class Directory(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, related_name='directories')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subdirectories', null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class File(models.Model):
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name
