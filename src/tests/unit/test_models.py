import pytest
from src.models import Product, Category, Coupon
from src.utils.calculations import calculate_discounted_price


@pytest.mark.django_db
class TestProductModel:
    def test_create_product(self, product: Product):
        assert product.name == "테스트 상품"
        assert product.price == 10000

    def test_product_discounted_price(self, product: Product):
        assert product.discounted_price == calculate_discounted_price(product.price, product.discount_rate)


@pytest.mark.django_db
class TestCategoryModel:
    def test_create_category(self, category: Category):
        assert category.name == "테스트 카테고리"


@pytest.mark.django_db
class TestCouponModel:
    def test_create_coupon(self, coupon: Coupon):
        assert coupon.code == "TEST2024"
        assert coupon.discount_rate == 0.2
