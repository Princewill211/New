# Generated by Django 5.0.1 on 2024-01-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_article_name_of_corresponding_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name_of_corresponding_author',
            field=models.CharField(default='name of corresponding author', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='type_of_articles',
            field=models.CharField(blank=True, choices=[('Short communication', 'Short communication'), ('Review article', 'Review article'), ('Research article', 'Research article')], max_length=200, null=True),
        ),
    ]
