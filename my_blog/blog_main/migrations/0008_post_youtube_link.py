# Generated by Django 3.1.5 on 2021-01-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_main', '0007_auto_20210117_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Youtube_link',
            field=models.URLField(blank=True),
        ),
    ]
