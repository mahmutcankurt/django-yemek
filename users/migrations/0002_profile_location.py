# Generated by Django 2.2.6 on 2019-11-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
