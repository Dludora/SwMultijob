# Generated by Django 3.2.5 on 2022-06-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_rename_description_article_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imginarticle',
            name='articleId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='imginarticle',
            name='userId',
            field=models.IntegerField(null=True),
        ),
    ]
