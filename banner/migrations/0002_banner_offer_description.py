# Generated by Django 4.2.7 on 2023-11-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='offer_description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
