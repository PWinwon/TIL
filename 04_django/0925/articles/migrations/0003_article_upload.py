# Generated by Django 3.2.7 on 2021-09-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_articles_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='upload',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
