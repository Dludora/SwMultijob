# Generated by Django 3.2.5 on 2022-06-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_author_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='lastLogout',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
