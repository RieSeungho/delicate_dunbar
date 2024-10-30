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
    following = models.ManyToManyField(
        'self', 
        verbose_name='팔로우 중인 사용자들',
        related_name='followers',
        symmetrical=False,
        through='users.Relationship'
    )

    def __str__(self):
        return self.username

    pass


class Relationship(models.Model):
    from_user = models.ForeignKey(
        'users.User',
        verbose_name= '팔로우를 요청한 사용자',
        related_name='following_relationships',
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        'users.User',
        verbose_name='팔로우 요청의 대상',
        related_name='followers_relationships',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'관계 ({self.from_user} -> {self.to_user})'