from rest_framework import serializers
from django.core.validators import MinValueValidator

from ..utils.http.response import get_pagination_response_serializer
from .http.request import _RequestQuerySerializerBase
from ..models.product import Product
from .category import GetCategorySerializer
from .coupon import GetCouponSerializer
from ..schema.product import GetProductDetailSchema, GetCouponForProductSchema
from ..utils.http.response import response_to_serializer


class GetProductsQuerySerializer(_RequestQuerySerializerBase):
    category_idx = serializers.IntegerField(required=False)


class GetProductSerializer(serializers.ModelSerializer):
    discounted_price: int = serializers.IntegerField(required=True, validators=[MinValueValidator(0)])
    category = GetCategorySerializer()

    class Meta:
        model = Product
        fields = [
            "idx",
            "name",
            "price",
            "description",
            "category",
            "discount_rate",
            "discounted_price",
            "coupon_applicable",
        ]


GetPaginationProductsSerializer = get_pagination_response_serializer(GetProductSerializer)


GetPaginationProductsResponseSerializer = response_to_serializer(GetPaginationProductsSerializer(many=False))


class GetProductDetailSerializer(GetProductSerializer):
    coupons = GetCouponSerializer(required=True, many=True)

    def to_representation(self, instance: GetProductDetailSchema) -> GetProductSerializer:
        data = {
            "idx": instance["product"].idx,
            "name": instance["product"].name,
            "price": instance["product"].price,
            "description": instance["product"].description,
            "category": instance["product"].category,
            "discount_rate": instance["product"].discount_rate,
            "discounted_price": instance["product"].discounted_price,
            "coupon_applicable": instance["product"].coupon_applicable,
            "coupons": (
                [
                    GetCouponForProductSchema(coupon=coupon, product=instance["product"])
                    for coupon in instance["coupons"]
                ]
                if instance["product"].coupon_applicable
                else []
            ),
        }
        return super().to_representation(data)

    class Meta:
        model = Product
        fields = [
            "idx",
            "name",
            "price",
            "description",
            "category",
            "discount_rate",
            "discounted_price",
            "coupon_applicable",
            "coupons",
        ]


GetProductDetailResponseSerializer = response_to_serializer(GetProductDetailSerializer(many=False))
