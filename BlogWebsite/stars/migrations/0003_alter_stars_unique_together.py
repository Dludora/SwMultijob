# Generated by Django 4.0.4 on 2022-06-07 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0002_alter_stars_articleid_alter_stars_userid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stars',
            unique_together={('userId', 'articleId')},
        ),
    ]
