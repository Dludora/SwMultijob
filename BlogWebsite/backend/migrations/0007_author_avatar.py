# Generated by Django 3.2.5 on 2022-06-08 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_author_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
