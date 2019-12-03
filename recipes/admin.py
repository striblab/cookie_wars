from django.contrib import admin

from .models import Baker, RecipeFeature, Recipe, RecipePhoto, BakerPhoto


class BakerAdmin(admin.ModelAdmin):
    pass


class BakerInline(admin.StackedInline):
    model = Recipe.baker.through
    extra = 1


class RecipePhotoInline(admin.StackedInline):
    readonly_fields = ['image_sized',]
    model = RecipePhoto
    extra = 1


class BakerPhotoInline(admin.StackedInline):
    model = BakerPhoto
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'get_baker')
    list_filter = ('year',)
    search_fields = ('name', 'ingredients', 'procedure')
    inlines = [BakerInline, RecipePhotoInline, BakerPhotoInline]
    exclude = ['baker']

    def get_baker(self, obj):
        return obj.baker.first()
    get_baker.short_description = 'Baker'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Baker, BakerAdmin)
admin.site.register(RecipeFeature)
