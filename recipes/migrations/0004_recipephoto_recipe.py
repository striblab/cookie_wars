# Generated by Django 2.2.7 on 2019-11-06 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipephoto',
            name='recipe',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
            preserve_default=False,
        ),
    ]
