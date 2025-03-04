import abc
import math
from typing import Sequence, Optional

from ..models.product import Product
from ._adaptor.product import ProductUseCaseAdaptor
from ._adaptor.coupon import CouponUseCaseAdaptor
from ..schema.product import GetProductDetailSchema
from ..exception.product import ProductNotFoundError


class GetProductsUseCase(metaclass=abc.ABCMeta):
    def __init__(self, product_adaptor: ProductUseCaseAdaptor):
        self.product_adaptor = product_adaptor

    def execute(self, category_idx: Optional[int] = None) -> Sequence[Product]:
        return self.product_adaptor.get_products(category_idx)


class GetProductDetailUseCase(metaclass=abc.ABCMeta):
    def __init__(self, product_adaptor: ProductUseCaseAdaptor, coupon_adaptor: CouponUseCaseAdaptor):
        self.product_adaptor = product_adaptor
        self.coupon_adaptor = coupon_adaptor

    def execute(self, product_idx: int) -> GetProductDetailSchema:
        try:
            product = self.product_adaptor.get_product(product_idx)
        except Exception:
            raise ProductNotFoundError()
        coupons = self.coupon_adaptor.get_coupons()
        return GetProductDetailSchema(product=product, coupons=coupons)
