# Generated by Django 5.0.1 on 2024-01-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_article_name_of_corresponding_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type_of_articles',
            field=models.CharField(blank=True, choices=[('Research article', 'Research article'), ('Short communication', 'Short communication'), ('Review article', 'Review article')], max_length=200, null=True),
        ),
    ]
