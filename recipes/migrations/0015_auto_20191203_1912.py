# Generated by Django 2.2.7 on 2019-12-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_auto_20191203_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipephoto',
            name='image_sized',
            field=models.ImageField(null=True, upload_to='recipes/resized'),
        ),
    ]
