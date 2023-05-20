from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """
    model to hold user details
    """
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_user_name = models.CharField(max_length=50, null=True, blank=True)
    profile_email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.profile_user.username
