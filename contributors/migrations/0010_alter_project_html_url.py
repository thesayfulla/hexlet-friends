# Generated by Django 4.1.2 on 2022-11-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0009_repository_owner_alter_repository_contributors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='html_url',
            field=models.URLField(),
        ),
    ]