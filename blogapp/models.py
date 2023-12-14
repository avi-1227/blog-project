from django.db import models
# Adding datetime fields
from django.utils import timezone

# Adding a many-to-one relationship
from django.contrib.auth.models import User

from django.urls import reverse


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]
    def __str__(self):
        return self.title
    

    # Using canonical URLs for models get_absolute_url()
    def get_absolute_url(self):
        return reverse('blogapp:post_detail', args=[self.id])

# Creating a model for comments
class Comment(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=90)
    email = models.EmailField()
    body = models.TextField()
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.MALE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering=['created']
        indexes = models.Index(fields=['created']),
    
    def __str__(self):
        return f'Comments by {self.name} on {self.post}'
