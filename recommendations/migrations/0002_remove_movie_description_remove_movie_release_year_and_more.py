# Generated by Django 4.2.5 on 2024-02-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_year',
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
