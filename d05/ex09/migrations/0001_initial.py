# Generated by Django 3.2 on 2021-05-06 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('climate', models.TextField(null=True)),
                ('diameter', models.IntegerField(null=True)),
                ('orbital_period', models.IntegerField(null=True)),
                ('population', models.BigIntegerField(null=True)),
                ('rotation_period', models.IntegerField(null=True)),
                ('surface_water', models.FloatField(null=True)),
                ('terrain', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('birth_year', models.CharField(max_length=32, null=True)),
                ('gender', models.CharField(max_length=32, null=True)),
                ('eye_color', models.CharField(max_length=32, null=True)),
                ('hair_color', models.CharField(max_length=32, null=True)),
                ('height', models.IntegerField(null=True)),
                ('mass', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('homeworld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ex09.planet')),
            ],
        ),
    ]