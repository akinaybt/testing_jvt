from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


