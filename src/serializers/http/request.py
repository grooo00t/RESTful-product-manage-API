from rest_framework import serializers


class _RequestQuerySerializerBase(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    size = serializers.IntegerField(required=False, default=20)

    def to_representation(self, instance: dict) -> dict:
        return {k: v for k, v in instance.items() if k not in ["page", "size"]}

    class Meta:
        abstract = True
