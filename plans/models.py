from django.contrib.auth.models import User
from django.db import models
from profiles.models import Profile


# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    image_field = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    plan = models.ForeignKey(
        Plan, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        Profile, related_name='plan_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.user.username} on {self.plan.name}'
