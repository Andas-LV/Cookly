from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models import Ingredient
from ..serializers import IngredientSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_ingredients(request):
    products = Ingredient.objects.all()
    serializer = IngredientSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_ingredient_by_id(request, ingredient_id):
    try:
        ingredient = Ingredient.objects.get(id=ingredient_id)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Ingredient.DoesNotExist:
        return Response({'error': 'Ингредиент не найден'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favourite(request, ingredient_id):
    try:
        ingredient = Ingredient.objects.get(id=ingredient_id)
        ingredient.is_favourite = not ingredient.is_favourite
        ingredient.save()
        return Response({
            'ingredient_name': ingredient.name,
            'is_favourite': ingredient.is_favourite
        }, status=status.HTTP_200_OK)
    except Ingredient.DoesNotExist:
        return Response({'error': 'Ингредиент не найден'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_basket(request, ingredient_id):
    try:
        ingredient = Ingredient.objects.get(id=ingredient_id)
        ingredient.in_basket = not ingredient.in_basket
        ingredient.save()
        return Response({
            'ingredient_name': ingredient.name,
            'in_basket': ingredient.in_basket
        }, status=status.HTTP_200_OK)
    except Ingredient.DoesNotExist:
        return Response({'error': 'Ингредиент не найден'}, status=status.HTTP_404_NOT_FOUND)
