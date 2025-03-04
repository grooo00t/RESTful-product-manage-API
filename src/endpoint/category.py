from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from ..serializers.category import GetCategoriesResponseSerializer
from ..service.category import GetCategoriesService


class CategoryManageView(APIView):
    @swagger_auto_schema(
        operation_description="카테고리 목록 조회",
        responses={200: GetCategoriesResponseSerializer},
        tags=["category"],
    )
    def get(self, _: Request):
        res = GetCategoriesService().execute()
        return Response(GetCategoriesResponseSerializer(res).data, 200)
