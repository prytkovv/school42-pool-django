# Generated by Django 3.2.2 on 2021-05-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0004_alter_vote_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='choice',
            field=models.CharField(max_length=2),
        ),
    ]
