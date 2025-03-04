from typing import Sequence

from ...usecase._adaptor.coupon import CouponUseCaseAdaptor
from ...models.coupon import Coupon


class CouponServiceAdaptor(CouponUseCaseAdaptor):
    def get_coupons(self) -> Sequence[Coupon]:
        return Coupon.objects.all()
