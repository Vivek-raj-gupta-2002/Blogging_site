# Generated by Django 3.1.5 on 2021-01-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_main', '0006_auto_20210117_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]