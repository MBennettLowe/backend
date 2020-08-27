# Generated by Django 2.2.4 on 2020-08-27 00:36

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import osprojects.models
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tagging', '0003_auto_20200508_1230'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OSProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid1, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('project_creator', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=600)),
                ('url', models.URLField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('open_to_contributors', models.BooleanField()),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='tagging.TaggedItems', to='tagging.CustomTag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=models.SET(osprojects.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
