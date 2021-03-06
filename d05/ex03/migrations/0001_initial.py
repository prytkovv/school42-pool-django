# Generated by Django 3.2 on 2021-05-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=64, unique=True)),
                ('episode_nb', models.AutoField(primary_key=True, serialize=False, verbose_name='episode_number')),
                ('opening_crawl', models.TextField(null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
