from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status
from fake_data.actions.fake_data_action import FakeDataAction


@api_view(['POST'])
def post(request):
    if 'data' in request.data:
        count = request.data['count'] if 'count' in request.data else 1
        result = FakeDataAction.get_data(request.data['data'], count)
        return Response(result, status=status.HTTP_200_OK)
    return Response({'error': 'please send your fields by using data as your key'})


class GetFakeData(APIView):
    def get(self, request):
        return Response(str(request.auth), status.HTTP_200_OK)

