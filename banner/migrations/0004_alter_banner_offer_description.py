# Generated by Django 4.2.7 on 2023-11-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_alter_banner_offer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='offer_description',
            field=models.CharField(max_length=100),
        ),
    ]