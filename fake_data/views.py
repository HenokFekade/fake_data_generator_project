from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from fake_data.actions.fake_data_action import FakeDataAction


@api_view(['POST'])
def post_without_saving(request):
    data, status = FakeDataAction.get_data_without_saving(request)
    return Response(data=data, status=status)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_with_auto_save(request):
    data, status = FakeDataAction.get_data_with_auto_save(request)
    return Response(data=data, status=status)

