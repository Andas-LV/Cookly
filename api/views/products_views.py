from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer, RecipeSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recipes_by_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        recipes = product.recipes.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found.'}, status=404)

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
        return Response({'message': 'Product image updated successfully.'}, status=200)
    return Response({'error': 'No image file provided.'}, status=400)