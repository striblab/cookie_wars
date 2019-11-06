# Generated by Django 2.2.7 on 2019-11-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20191106_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recipes')),
                ('cutline', models.TextField()),
                ('priority', models.IntegerField(default=2)),
            ],
        ),
    ]
