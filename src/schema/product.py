from typing import TypedDict, Sequence

from ..models.product import Product
from ..models.coupon import Coupon


class GetProductDetailSchema(TypedDict):
    product: Product
    coupons: Sequence[Coupon]


class GetCouponForProductSchema(TypedDict):
    coupon: Coupon
    product: Product
