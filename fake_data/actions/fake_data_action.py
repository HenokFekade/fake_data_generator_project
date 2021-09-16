import random
import json
from jsonfield.fields import JSONEncoder

from faker import Faker
from rest_framework import status

from fake_data.serializer import FakeDataSerializer


class FakeDataAction:
    _faker = Faker()

    @staticmethod
    def get_data_with_auto_save(request):
        data, my_status = FakeDataAction._get_data(request)
        if my_status == status.HTTP_200_OK:
            serializer = FakeDataSerializer(data=({'user_id': request.user.id, 'data': json.dumps(data, cls=JSONEncoder)}))
            if serializer.is_valid():
                serializer.create(serializer.data)
                return data, my_status
            else:
                return serializer.errors, status.HTTP_400_BAD_REQUEST
        else:
            return data, my_status

    @staticmethod
    def get_data_without_saving(request):
        return FakeDataAction._get_data(request)

    @staticmethod
    def _get_data(request):
        if 'data' in request.data:
            count = request.data['count'] if 'count' in request.data else 1
            fields = request.data['data']
            data = []
            count = FakeDataAction._get_count(count)

            for i in range(0, count):
                result = {}
                for field in fields:
                    result[field] = FakeDataAction._get_fake_data(field)
                data.append(result)
            return data, status.HTTP_200_OK
        else:
            return {'error': 'please send your fields by using data as your key'}, status.HTTP_400_BAD_REQUEST

    @staticmethod
    def _get_count(count):
        try:
            count = int(count)
        except ValueError:
            raise ValueError('The count field must be integer.')
        return count

    @staticmethod
    def _get_fake_data(field):

        if field == 'full_name':
            return FakeDataAction._faker.name()
        elif field == 'first_name':
            return FakeDataAction._faker.first_name()
        elif field == 'last_name':
            return FakeDataAction._faker.last_name()
        elif field == 'gender':
            return random.choice(['male', 'female'])
        elif field == 'age':
            return random.randint(1, 99)
        elif field == 'job':
            return FakeDataAction._faker.job()
        elif field == 'location':
            location = {'lat': FakeDataAction._faker.latitude(), 'lon': FakeDataAction._faker.longitude()}
            return location
        elif field == 'job':
            return FakeDataAction._faker.job()
        elif field == 'email':
            return FakeDataAction._faker.email()
        elif field == 'address':
            return FakeDataAction._faker.address()
        else:
            return 'field not found'
