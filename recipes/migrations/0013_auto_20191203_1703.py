# Generated by Django 2.2.7 on 2019-12-03 17:03

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_recipe_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipephoto',
            name='std_image',
            field=stdimage.models.StdImageField(null=True, upload_to='recipes/std'),
        ),
        migrations.AlterField(
            model_name='recipephoto',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='recipes.Recipe'),
        ),
    ]