from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from ._base import _BaseModel


class Coupon(_BaseModel):
    """
    Coupon 모델:

    - code: 쿠폰 코드 (문자열, 고유값)
    - discount_rate: 쿠폰 할인율 (소수점)
    """

    code: str = models.CharField(max_length=50, unique=True)
    discount_rate: float = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])

    class Meta:
        db_table = "coupon"
