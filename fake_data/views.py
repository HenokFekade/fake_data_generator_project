from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from fake_data.actions.fake_data_action import FakeDataAction


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post(request):
    data, status = FakeDataAction.get_data(request)
    return Response(data=data, status=status)



