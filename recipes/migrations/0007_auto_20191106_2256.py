# Generated by Django 2.2.7 on 2019-11-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20191106_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakerphoto',
            name='credit',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='recipephoto',
            name='credit',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
