# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-23 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20180422_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='myList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='wish',
            name='uploaded_by_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='first_app.User'),
        ),
    ]