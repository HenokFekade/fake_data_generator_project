import json
import random

from faker import Faker
from rest_framework import status

from fake_data.serializer import FakeDataSerializer


class FakeDataAction:
    faker = Faker()

    @staticmethod
    def get_data(request):
        if 'data' in request.data:
            count = request.data['count'] if 'count' in request.data else 1
            fields = request.data['data']
            data = []
            count = FakeDataAction.get_count(count)

            for i in range(0, count):
                result = {}
                for field in fields:
                    result[field] = FakeDataAction._get_fake_data(field)
                data.append(result)
            # serializer = FakeDataSerializer(data=({'user_id': request.user.id, 'data': json.dumps(data)}))
            # if serializer.is_valid():
            #     serializer.create(serializer.data)
            print(json.dumps({'data': data}))
            return data, status.HTTP_200_OK
        else:
            return {'error': 'please send your fields by using data as your key'}, status.HTTP_400_BAD_REQUEST

    @staticmethod
    def get_count(count):
        try:
            count = int(count)
        except ValueError:
            raise ValueError('The count field must be integer.')
        return count

    @staticmethod
    def _get_fake_data(field):

        if field == 'full_name':
            return FakeDataAction.faker.name()
        elif field == 'first_name':
            return FakeDataAction.faker.first_name()
        elif field == 'last_name':
            return FakeDataAction.faker.last_name()
        elif field == 'gender':
            return random.choice(['male', 'female'])
        elif field == 'age':
            return random.randint(1, 99)
        elif field == 'job':
            return FakeDataAction.faker.job()
        elif field == 'location':
            location = {'lat': FakeDataAction.faker.latitude(), 'lon': FakeDataAction.faker.longitude()}
            return location
        elif field == 'job':
            return FakeDataAction.faker.job()
        elif field == 'email':
            return FakeDataAction.faker.email()
        elif field == 'address':
            return FakeDataAction.faker.address()
        else:
            return 'field not found'
