# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0008_auto_20160726_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlereview',
            name='user',
        ),
        migrations.AddField(
            model_name='articlereview',
            name='contributors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articlereview',
            name='original_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='article_original_author_of', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]