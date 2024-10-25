from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Recipe
from ..serializers import RecipeSerializer, RecipeDetailSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recipe_products(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        serializer = RecipeDetailSerializer(recipe)
        return Response(serializer.data)
    except Recipe.DoesNotExist:
        return Response({'error': 'Recipe not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_recipe_image(request, id):
    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response({'error': 'Recipe does not exist.'}, status=404)

    if 'image' in request.FILES:
        recipe.image = request.FILES['image']
        recipe.save()
        return Response({'message': 'Recipe image updated successfully.'}, status=200)
    return Response({'error': 'No image file provided.'}, status=400)