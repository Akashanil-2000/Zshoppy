# Generated by Django 4.2.7 on 2023-11-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0006_rename_is_deleted_product_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]