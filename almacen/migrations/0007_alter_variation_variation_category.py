# Generated by Django 4.2.1 on 2023-05-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("almacen", "0006_rename_producto_variation_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="variation",
            name="variation_category",
            field=models.CharField(
                choices=[("color", "color"), ("tamaño", "size")], max_length=100
            ),
        ),
    ]
