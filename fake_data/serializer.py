from rest_framework import serializers

from fake_data.models import FakeData


class FakeDataSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    data = serializers.JSONField()

    def create(self, validated_data):
        fake_data = FakeData.objects.create(validated_data)
        return fake_data
