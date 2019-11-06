from django.db import models


class Baker(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    full_name_override = models.CharField(max_length=100, blank=True)
    hometown = models.CharField(max_length=100)


class Recipe(models.Model):
    baker = models.ForeignKey(Baker, null=True, on_delete=models.SET_NULL)
    year
    recipe_yield
    ingredients
    procedure
