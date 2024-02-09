# Generated by Django 5.0.1 on 2024-02-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_article_pdf_upload_alter_article_type_of_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type_of_articles',
            field=models.CharField(blank=True, choices=[('Research article', 'Research article'), ('Review article', 'Review article'), ('Short communication', 'Short communication')], max_length=200, null=True),
        ),
    ]
