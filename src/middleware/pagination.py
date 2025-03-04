from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.serializers import Serializer


class MainPageNumberPagination(PageNumberPagination):
    page_size_query_param = "size"
    page_size = 30

    def get_paginated_response(self, data: dict, serializer: Serializer, status_code: int = 200):
        serialized_data = serializer(data, many=True)
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": serialized_data.data,
            },
            status_code,
        )
