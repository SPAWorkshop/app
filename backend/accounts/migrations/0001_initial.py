# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=75, db_index=True, unique=True)),
                ('is_active', models.BooleanField(default=True, db_index=True)),
                ('is_staff', models.BooleanField(default=False, db_index=True)),
                ('first_logged_at', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', related_name='user_set', related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.')),
                ('user_permissions', models.ManyToManyField(blank=True, to='auth.Permission', related_name='user_set', related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
