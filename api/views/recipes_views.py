from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Recipes
from ..serializers import RecipeSerializer, RecipeByCategorySerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recipes_by_category(request, category):
    recipes = Recipes.objects.filter(category=category)
    if recipes.exists():
        serializer = RecipeByCategorySerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'Рецепты с данной категорией не найдены'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recipe_by_id(request, recipe_id):
    try:
        recipe = Recipes.objects.get(id=recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Recipes.DoesNotExist:
        return Response({'error': 'Рецепт не найден'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_recipe_favourite(request, recipe_id):
    try:
        recipe = Recipes.objects.get(id=recipe_id)
        recipe.is_favourite = not recipe.is_favourite
        recipe.save()
        return Response({
            'recipe_name': recipe.name,
            'is_favourite': recipe.is_favourite
        }, status=status.HTTP_200_OK)
    except Recipes.DoesNotExist:
        return Response({'error': 'Рецепт не найден'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_recipe_basket(request, recipe_id):
    try:
        recipe = Recipes.objects.get(id=recipe_id)
        recipe.in_basket = not recipe.in_basket
        recipe.save()
        return Response({
            'recipe_name': recipe.name,
            'in_basket': recipe.in_basket
        }, status=status.HTTP_200_OK)
    except Recipes.DoesNotExist:
        return Response({'error': 'Рецепт не найден'}, status=status.HTTP_404_NOT_FOUND)