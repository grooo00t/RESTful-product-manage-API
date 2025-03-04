from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from ..exception.product import ProductNotFoundError
from ..utils.http.response import error_to_serializer
from ..middleware.pagination import MainPageNumberPagination
from ..serializers.product import (
    GetProductsQuerySerializer,
    GetProductSerializer,
    GetPaginationProductsResponseSerializer,
    GetProductDetailResponseSerializer,
)
from ..service.product import GetProductsService, GetProductDetailService


class ProductManageView(APIView):
    @swagger_auto_schema(
        operation_description="상품 목록 조회",
        query_serializer=GetProductsQuerySerializer,
        responses={200: GetPaginationProductsResponseSerializer},
        tags=["product"],
    )
    def get(self, request: Request):
        query_serializer = GetProductsQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        response = GetProductsService().execute(**query_serializer.data)
        paginator = MainPageNumberPagination()
        queryset = paginator.paginate_queryset(response, request)
        res = paginator.get_paginated_response(queryset, GetProductSerializer, 200)
        return Response(GetPaginationProductsResponseSerializer(res.data).data, 200)


class ProductDetailManageView(APIView):
    @swagger_auto_schema(
        operation_description="상품 상세 정보 조회",
        responses={
            200: GetProductDetailResponseSerializer,
            404: error_to_serializer(ProductNotFoundError),
        },
        tags=["product"],
    )
    def get(self, _: Request, product_idx: int):
        response = GetProductDetailService().execute(product_idx)
        return Response(GetProductDetailResponseSerializer(response).data, 200)
