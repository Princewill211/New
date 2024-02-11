# Generated by Django 5.0.1 on 2024-02-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_article_type_of_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type_of_articles',
            field=models.CharField(blank=True, choices=[('Review article', 'Review article'), ('Research article', 'Research article'), ('Short communication', 'Short communication'), ('Case study', 'Case study')], max_length=200, null=True),
        ),
    ]
