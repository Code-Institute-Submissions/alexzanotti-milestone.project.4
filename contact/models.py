from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Contact(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Assigned', 'Assigned'),
        ('In Progress', 'In Progress'),
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Comment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.text}'
