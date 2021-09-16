from rest_framework import serializers

from fake_data.models import FakeData
from users.models import CustomUser


class FakeDataSerializer(serializers.Serializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    data = serializers.JSONField()

    def create(self, validated_data):
        user = self.get_user(validated_data)
        fake_data = FakeData.objects.create(user_id=user, data=validated_data['data'])
        return fake_data

    def get_user(self, validated_data):
        """
        Return current authenticated user.
        @rtype: object
        """
        user = CustomUser.objects.get(pk=validated_data['user_id'])
        return user

