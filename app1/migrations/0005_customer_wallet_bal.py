# Generated by Django 4.2.7 on 2023-11-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_product_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='wallet_bal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
