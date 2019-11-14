from rest_framework import serializers

from .models import Recipe, Baker, RecipePhoto


# class RecipeFeatureSerializer(serializers.Model)


class BakerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='__str__')

    class Meta:
        model = Baker
        fields = ['name', 'hometown']


# class RecipePhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipePhoto
#         fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    baker = BakerSerializer(many=True, read_only=True)
    # photos = RecipePhotoSerializer(many=True, read_only=True)
    features = serializers.StringRelatedField(many=True)
    cookie_type = serializers.CharField(source='get_cookie_type_display')

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'summary', 'baker', 'features', 'cookie_type', 'year', 'recipe_yield', 'ingredients_clean', 'procedure', 'notes', 'baker_bio_notes', 'thumbnail']
