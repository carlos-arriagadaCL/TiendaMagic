# Generated by Django 4.2.1 on 2023-05-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categoria", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoria",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
