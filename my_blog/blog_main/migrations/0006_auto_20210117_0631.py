# Generated by Django 3.1.5 on 2021-01-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_main', '0005_auto_20210117_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]