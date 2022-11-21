from rest_framework import serializers
from .models import Post, Student,Restaurant,Recipe,Ingredient,Snippet,Musician
import base64
from django.conf import settings
import os

class PostSerializer( serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'




class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    # Serializer for the Restaurant model, in fields we specify the model attributes we want to
    # deserialize and serialize
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'direction', 'phone']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    
    # As each recipe has an image thumbnail we deal with the serialization of the image in the function
    # 'encode_thumbnail' were the image is read from the media folder and encoded into base64
    thumbnail = serializers.SerializerMethodField('encode_thumbnail')
    # When getting a recipe I want an 'ingredients' field, the value of this field is the return of the get_ingredients
    # function that serializes the ingredients for the recipe.
    ingredients = serializers.SerializerMethodField('get_ingredients')

    def encode_thumbnail(self, recipe):
        with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), "rb") as image_file:
            return base64.b64encode(image_file.read())

    def get_ingredients(self, recipe):
        try:
            recipe_ingredients = Ingredient.objects.filter(recipe__id=recipe.id)
            return IngredientSerializer(recipe_ingredients, many=True).data
        except Ingredient.DoesNotExist:
            return None

    def create(self, validated_data):
        """
        Create function for recipes, a restaurant and a list of ingredients is asociated. The restaurantId
        is taken from the corresponding path parameter and the ingredients can be added optionally in the post body.
        """
        ingredients_data = validated_data.pop("ingredients")

        restaurant = Restaurant.objects.get(pk=validated_data["restaurant_id"])
        validated_data["restaurant"] = restaurant
        recipe = Recipe.objects.create(**validated_data)

        # Assign ingredients if they are present in the body
        if ingredients_data:
            for ingredient_dict in ingredients_data:
                ingredient = Ingredient(name=ingredient_dict["name"])
                ingredient.save()
                ingredient.recipe.add(recipe)
        return recipe

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'type', 'thumbnail', 'ingredients']       


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style', )      


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = '__all__'                           