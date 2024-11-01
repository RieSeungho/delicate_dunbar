# Generated by Django 4.2.16 on 2024-10-30 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='candidate_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_posts', to=settings.AUTH_USER_MODEL, verbose_name='대상자'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일시'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='삭제일시'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일시'),
        ),
        migrations.AlterField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='삭제일시'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_posts', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
