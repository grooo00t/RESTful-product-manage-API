from typing import Union

from rest_framework import serializers

from ...exception import _BaseError
from ...serializers.http.response import _PaginationSerializerBase, _ResponseSerializer


def get_pagination_response_serializer(
    result_serializer: Union[type[serializers.Serializer], serializers.Serializer]
) -> type[_PaginationSerializerBase]:
    return type(
        f"{result_serializer.__name__}PaginationSerializer",
        (_PaginationSerializerBase,),
        {
            "results": result_serializer(many=True),
        },
    )


def response_to_serializer(
    data_serializer: Union[type[serializers.Serializer], serializers.Serializer, None] = None
) -> type[_ResponseSerializer]:
    if data_serializer is None:
        return type(
            "",
            (_ResponseSerializer,),
            {
                "code": serializers.CharField(default="0"),
                "message": serializers.CharField(default="Success"),
            },
        )
    else:
        return type(
            "",
            (_ResponseSerializer,),
            {
                "code": serializers.CharField(default="0"),
                "message": serializers.CharField(default="Success"),
                "data": data_serializer,
            },
        )


def error_to_serializer(error: Union[type[_BaseError], _BaseError]) -> type[serializers.Serializer]:
    return type(
        "",
        (serializers.Serializer,),
        {
            "code": serializers.CharField(default=error.code()),
            "message": serializers.CharField(default=error.message()),
        },
    )
