# Generated by Django 3.2.6 on 2023-10-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_authorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
