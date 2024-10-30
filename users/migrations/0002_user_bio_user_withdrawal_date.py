# Generated by Django 4.2.16 on 2024-10-29 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='withdrawal_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
