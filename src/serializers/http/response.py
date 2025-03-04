from typing import Union, Optional
from rest_framework import serializers


class _ResponseSerializer(serializers.Serializer):
    code = serializers.CharField()
    message = serializers.CharField()

    def to_representation(self, instance: Optional[dict] = None):
        res = {} if instance is None else {"data": instance}
        return super().to_representation(res)

    class Meta:
        abstract = True


class _PaginationSerializerBase(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.URLField(allow_null=True)
    previous = serializers.URLField(allow_null=True)

    class Meta:
        abstract = True
