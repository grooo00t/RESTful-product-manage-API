import pytest
from rest_framework.test import APIClient
from src.models import Category, Product, Coupon


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def category_data():
    return {
        "name": "테스트 카테고리",
    }


@pytest.fixture
def product_data():
    return {
        "name": "테스트 상품",
        "description": "테스트 상품 설명",
        "price": 10000,
        "discount_rate": 0.1,
        "coupon_applicable": True,
    }


@pytest.fixture
def coupon_data():
    return {
        "code": "TEST2024",
        "discount_rate": 0.2,
    }


@pytest.fixture
def category(db):
    return Category.objects.create(name="테스트 카테고리")


@pytest.fixture
def product(db, category):
    return Product.objects.create(
        name="테스트 상품",
        description="테스트 상품 설명",
        price=10000,
        category=category,
        discount_rate=0.1,
        coupon_applicable=True,
    )


@pytest.fixture
def coupon(db):
    return Coupon.objects.create(
        code="TEST2024",
        discount_rate=0.2,
    )
