# Generated by Django 3.0.5 on 2020-07-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20200716_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatorinfo',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
