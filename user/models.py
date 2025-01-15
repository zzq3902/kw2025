from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=11)
    birth_date = models.DateTimeField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.user.username
