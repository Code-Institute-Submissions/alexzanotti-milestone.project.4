from django.db import models
from profiles.models import Profile

# Create your models here.


class Donation(models.Model):
    """
    Model to hold donation details
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    donated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.profile.profile_user.username} donation status: {self.donated}'
