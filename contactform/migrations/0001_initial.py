# Generated by Django 2.2.9 on 2020-03-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm_queries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=54)),
                ('subject', models.CharField(max_length=54)),
                ('message', models.CharField(max_length=1154)),
            ],
        ),
    ]
