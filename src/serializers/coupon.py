from django.core.validators import MinValueValidator
from rest_framework import serializers
from ..models.coupon import Coupon
from ..schema.product import GetCouponForProductSchema
from ..utils.calculations import calculate_discounted_price


class GetCouponSerializer(serializers.ModelSerializer):
    discounted_price: int = serializers.IntegerField(required=True, validators=[MinValueValidator(0)])

    def to_representation(self, instance: GetCouponForProductSchema):
        data = {
            "code": instance["coupon"].code,
            "discount_rate": instance["coupon"].discount_rate,
            "discounted_price": calculate_discounted_price(
                instance["product"].discounted_price, instance["coupon"].discount_rate
            ),
        }
        return data

    class Meta:
        model = Coupon
        fields = ["code", "discount_rate", "discounted_price"]
