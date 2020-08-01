from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User, null=True, blank=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='', blank=True)
    status = models.CharField(max_length=10, choices=[
                              ('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[
                              ('A', 'active'), ('D', 'depricated')])

    def __str__(self):
        return self.title


# class PostCategories(models.Model):
#     posts = models.ForeignKey(Post, on_delete=models.CASCADE)
#     categoryies = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.posts} относится к {self.categoryies}'
