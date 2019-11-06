from django.db import models


class Baker(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    full_name_override = models.CharField(max_length=100, blank=True)
    hometown = models.CharField(max_length=100)
    # notes = models.TextField(blank=True)

    def __str__(self):
        if self.full_name_override != '':
            return self.full_name_override
        return '{} {}'.format(self.first_name, self.last_name)


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    baker = models.ManyToManyField(Baker)
    year = models.IntegerField()
    recipe_yield = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    baker_bio_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class RecipePhoto(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes')
    cutline = models.TextField(blank=True)
    credit = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(default=2)


class BakerPhoto(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bakers')
    cutline = models.TextField(blank=True)
    credit = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(default=2)
