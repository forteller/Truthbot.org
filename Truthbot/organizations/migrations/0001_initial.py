# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 10:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=2083)),
                ('wiki_url', models.CharField(max_length=2083)),
                ('child_organizations', models.ManyToManyField(blank=True, related_name='parent_organizations', to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=200, unique=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tone', models.CharField(choices=[('P', 'Positive'), ('N', 'Neutral'), ('C', 'Critical')], default='N', max_length=1)),
                ('text', models.CharField(max_length=3000)),
                ('points', models.IntegerField(default=1)),
                ('contributors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization')),
                ('original_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_author_of', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
