import random

from faker import Faker


class FakeDataAction:
    faker = Faker()

    @staticmethod
    def get_data(fields, count):
        data = []
        try:
            count = int(count)
        except ValueError:
            raise ValueError('The count field must be integer.')

        for i in range(0, count):
            result = {}
            for field in fields:
                result[field] = FakeDataAction._get_fake_data(field)
            data.append(result)
        return data

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
