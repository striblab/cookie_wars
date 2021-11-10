import os
import re
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# from django.core.files import File
from django.db import models
# from settings.storage_backends import MediaStorage

# from stdimage import StdImageField


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


class RecipeFeature(models.Model):
    name = models.CharField(max_length=25)
    sort_priority = models.IntegerField(default=2)

    def __str__(self):
        return self.name

COOKIE_TYPE_CHOICES = (
    ("Ro", "Rolled"),
    ("B", "Bar"),
    ("D", "Drop"),
    ("Rf", "Refrigerator"),
)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True)
    baker = models.ManyToManyField(Baker)
    features = models.ManyToManyField(RecipeFeature)
    cookie_type = models.CharField(max_length=4, choices=COOKIE_TYPE_CHOICES, blank=True)
    year = models.IntegerField()
    recipe_yield = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    procedure = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    baker_bio_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def ingredients_clean(self):
        # Let's find bullet listy things and make them <li>s
        output = self.ingredients
        section_heads = r'(For .*?:*)\r\n'
        output = re.sub(section_heads, r'</ul>\n<div><strong>\1</strong></div>\n<ul>\r\n', output)

        bullets_etc = r'((?:\r\n)+)(?:• )*'  # line breaks with optional bullets
        output = re.sub(bullets_etc, r'</li>\n<li>', output)
        output = re.sub(r'^', '<ul>\n<li>', output)  # Start every list with a <ul>
        output = re.sub(r'<li>• ', r'<li>', output)  # Clean up first bullet if it's one of those
        output = re.sub(r'$', r'</li>\n</ul>', output)  # Close the <li> and <ul> at the end
        output = output.replace('<li></ul>', '</ul>')  # Clean up
        output = output.replace('<ul></li>', '<ul>')  # Clean up
        output = re.sub(r'^<ul>\n</ul>\n', '', output)  # But if you start with a header trim that <ul> and excess off

        return output

    def clean_text(self, input):
        section_heads = r'(?:^|\r\n)([\w ’\']+?:)(?: |\r\n)'  # Any word-y things at the start of string or start of line followed by a : and then a space or line break
        output = re.sub(section_heads, r'\r\n<strong>\1</strong> ', input)
        output = re.sub(r'^\r\n', r'', output)
        output = re.sub(r'(?:\r\n)+', r'</p>\n<p>', output)
        return '<p>{}</p>'.format(output)

    @property
    def procedure_clean(self):
        return self.clean_text(self.procedure)

    @property
    def baker_bio_notes_clean(self):
        return self.clean_text(self.baker_bio_notes)

    @property
    def thumbnail(self):
        try:
            return self.photos.first().image_sized.url
        except:
            # return ''
            raise


class RecipePhoto(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes')
    image_sized = models.ImageField(upload_to='recipes/resized', null=True)
    cutline = models.TextField(blank=True)
    credit = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(default=2)

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        im = Image.open(self.image)
        output = BytesIO()
        # Get existing aspect ratio
        aspect_ratio = float(im.size[1]) / float(im.size[0])
        #Resize/modify the image
        im = im.resize((1000, int(1000.0 * aspect_ratio)))
        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        self.image_sized = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(RecipePhoto, self).save()


class BakerPhoto(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bakers')
    cutline = models.TextField(blank=True)
    credit = models.CharField(max_length=255, blank=True)
    priority = models.IntegerField(default=2)
