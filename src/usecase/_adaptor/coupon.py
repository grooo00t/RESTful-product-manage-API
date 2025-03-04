import abc
from typing import Sequence

from ...models.coupon import Coupon


class CouponUseCaseAdaptor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_coupons(self) -> Sequence[Coupon]: ...
