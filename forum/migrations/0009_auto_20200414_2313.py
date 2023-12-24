# Generated by Django 2.2 on 2020-04-14 17:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0008_answer_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='vote',
        ),
        migrations.AddField(
            model_name='answer',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]