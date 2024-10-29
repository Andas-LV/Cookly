from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from ..serializers import RegisterSerializer, UserSerializer, LoginSerializer
from ..models import Profile
from ..tasks import update_avatar_task

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
    avatar_file = request.FILES.get('avatar')
    if avatar_file:
        update_avatar_task.delay(request.user.id, avatar_file)

        return Response({
            'message': 'Avatar upload started successfully. It will be updated shortly.',
            'user': UserSerializer(request.user).data,
        })
    return Response({'error': 'No avatar file provided.'}, status=400)