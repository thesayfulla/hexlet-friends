# Generated by Django 2.2.5 on 2019-09-30 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190930_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='additions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contribution',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contribution',
            name='deletions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contribution',
            name='issues',
            field=models.IntegerField(default=0),
        ),
    ]