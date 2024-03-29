# Generated by Django 5.0.1 on 2024-02-10 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(default=datetime.datetime.now)),
                ('featured_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
