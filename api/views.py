from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (RegisterSerializer, UserSerializer, LoginSerializer,
                          RecipeSerializer, ProductSerializer,RecipeDetailSerializer)
from .models import Profile, Recipe, Product
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET'])
def index(request):
    return Response({"message": "ВСЕ РАБОТАЕТ."})

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        Profile.objects.create(user=user)
        return Response({
            'user': UserSerializer(user).data,
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    user = request.user
    return Response(UserSerializer(user).data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_avatar(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return Response({'error': 'User profile does not exist.'}, status=404)

    avatar_file = request.FILES.get('avatar')
    if avatar_file:
        profile.avatar = avatar_file
        profile.save()
        avatar_url = profile.avatar.url
        return Response({
            'message': 'Avatar updated successfully.',
            'user': UserSerializer(request.user).data,
            'avatar_url': avatar_url
        })
    return Response({'error': 'No avatar file provided.'}, status=400)

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

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

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product_image(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist.'}, status=404)

    if 'image' in request.FILES:
        product.image = request.FILES['image']
        product.save()
        return Response({'message': 'Recipe image updated successfully.'}, status=200)
    return Response({'error': 'No image file provided.'}, status=400)