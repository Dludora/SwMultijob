# Generated by Django 4.0.4 on 2022-06-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_like', '0004_alter_comments_articleid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=100000, null=True),
        ),
    ]
