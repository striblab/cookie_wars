from django.contrib import admin

from .models import Baker, Recipe, RecipePhoto, BakerPhoto


class BakerAdmin(admin.ModelAdmin):
    pass


class BakerInline(admin.TabularInline):
    model = Recipe.baker.through
    extra = 1


class RecipePhotoInline(admin.TabularInline):
    model = RecipePhoto
    extra = 1


class BakerPhotoInline(admin.TabularInline):
    model = BakerPhoto
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [BakerInline, RecipePhotoInline, BakerPhotoInline]
    exclude = ['baker']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Baker, BakerAdmin)
