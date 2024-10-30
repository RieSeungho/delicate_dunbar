from django.db import models

from users.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        'users.User',
        verbose_name='작성자',
        on_delete=models.CASCADE,
        related_name='author_posts',
    )
    candidate_user = models.ForeignKey(
        'users.User',
        verbose_name='대상자',
        on_delete=models.CASCADE,
        related_name='candidate_posts',
        null=True,
    )
    content = models.TextField('내용')
    tags = models.ManyToManyField('posts.HashTag', verbose_name='해시태그 목록', blank=True)
    created = models.DateTimeField("생성일시", auto_now_add=True)
    updated = models.DateTimeField("수정일시", auto_now=True)
    deleted = models.BooleanField('삭제여부', default=False)

    def __str__(self):
        return f"{self.user.username}의 Post(id: {self.id})"
    
class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='포스트',
        on_delete=models.CASCADE,
    )
    photo = models.ImageField("사진", upload_to="post")

class Comment(models.Model):
    user = models.ForeignKey(
        'users.User',
        verbose_name='작성자',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post, verbose_name='포스트', on_delete=models.CASCADE)
    content = models.TextField('내용')
    created = models.DateTimeField('생성일시', auto_now_add=True)
    updated = models.DateTimeField('수정일시', auto_now=True)
    deleted = models.BooleanField('삭제여부', default=False)

class HashTag(models.Model):
    name = models.CharField("태그명", max_length=50)

    def __str__(self):
        return self.name