# Generated by Django 5.0.1 on 2024-01-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_title_of_article_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
    ]
