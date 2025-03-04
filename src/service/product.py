from typing import Optional

from ..usecase.product import GetProductsUseCase, GetProductDetailUseCase
from ..usecase._adaptor.product import ProductUseCaseAdaptor
from ..usecase._adaptor.coupon import CouponUseCaseAdaptor
from ._adpator.product import ProductServiceAdaptor
from ._adpator.coupon import CouponServiceAdaptor


class GetProductsService(GetProductsUseCase):
    def __init__(self, product_adaptor: Optional[ProductUseCaseAdaptor] = None):
        super().__init__(product_adaptor or ProductServiceAdaptor())


class GetProductDetailService(GetProductDetailUseCase):
    def __init__(
        self,
        product_adaptor: Optional[ProductUseCaseAdaptor] = None,
        coupon_adaptor: Optional[CouponUseCaseAdaptor] = None,
    ):
        super().__init__(product_adaptor or ProductServiceAdaptor(), coupon_adaptor or CouponServiceAdaptor())
