from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ..utils.calculations import calculate_discounted_price
from ._base import _BaseModel
from .category import Category


class Product(_BaseModel):
    """
    Product 모델:

    - name : 상품 이름 (문자열, 최대 255자)
    - description: 상품 설명 (텍스트)
    - price: 상품 가격 (정수형, 기본 단위는 원)
    - category: 상품 카테고리 (외래키, Category 모델과 연결)
    - discount_rate: 할인율 (소수점, 예: 0.10은 10% 할인)
    - coupon_applicable: 쿠폰 적용 가능 여부 (boolean)
    """

    name: str = models.CharField(max_length=255)
    description: str = models.TextField()
    price: int = models.PositiveIntegerField()
    category: Category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    discount_rate: float = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])
    coupon_applicable: bool = models.BooleanField()

    @property
    def discounted_price(self) -> int:
        return calculate_discounted_price(self.price, self.discount_rate)

    class Meta:
        db_table = "product"
