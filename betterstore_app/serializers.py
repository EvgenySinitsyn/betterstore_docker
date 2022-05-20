from rest_framework import serializers


class JsonResponse:
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp


class JsonResponseSerializer(serializers.Serializer):
    value = serializers.JSONField(allow_null=True)
    timestamp = serializers.IntegerField()
