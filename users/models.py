from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='users/profile', blank=True)
    withdrawal_date = models.DateTimeField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    like_posts = models.ManyToManyField(
        'posts.Post', 
        verbose_name='좋아요 누른 Post 목록',
        related_name='like_users',
        blank=True,
    )

    pass

    def __str__(self):
        return self.username