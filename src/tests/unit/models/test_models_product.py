import pytest
from src.models import Product
from src.utils.calculations import calculate_discounted_price


@pytest.mark.django_db
class TestProductModel:
    def test_create_product(self, product: Product):
        assert product.name == "테스트 상품"
        assert product.price == 10000
        assert product.category is not None

    def test_product_discounted_price(self, product: Product):
        assert product.discounted_price == calculate_discounted_price(product.price, product.discount_rate)
