# Generated by Django 2.2.7 on 2019-12-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20191203_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipephoto',
            name='std_image',
        ),
        migrations.AddField(
            model_name='recipephoto',
            name='image_sized',
            field=models.ImageField(null=True, upload_to='recipes/sized'),
        ),
    ]
