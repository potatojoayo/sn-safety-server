# Generated by Django 4.0.2 on 2022-02-26 15:10

import django.contrib.postgres.fields
from django.db import migrations, models
import posting.models.introduction


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('meeting_id', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Debriefing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('meeting_id', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('files', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
                ('download', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course_introduction', models.TextField()),
                ('instructor_introduction', models.CharField(max_length=200)),
                ('instructor_name', models.CharField(max_length=10)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=posting.models.introduction.upload_to)),
                ('job', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('youtube_id', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('files', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('secret', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('survey_url', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField()),
                ('youtube_id', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
