# Generated by Django 2.2.7 on 2019-11-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20191107_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipefeature',
            name='sort_priority',
            field=models.IntegerField(default=2),
        ),
    ]