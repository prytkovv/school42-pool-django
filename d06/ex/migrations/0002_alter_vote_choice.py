# Generated by Django 3.2.2 on 2021-05-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='choice',
            field=models.CharField(choices=[('UP', 'UPVOTE'), ('DN', 'DOWNVOTE'), ('NO', 'NOVOTE')], default='NO', max_length=2),
        ),
    ]