from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.action.user_action import UserAction


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data, status = UserAction.register(request)
    return Response(data=data, status=status)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data, status = UserAction.login(request)
    return Response(data=data, status=status)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    data, status = UserAction.logout(request)
    return Response(data=data, status=status)
