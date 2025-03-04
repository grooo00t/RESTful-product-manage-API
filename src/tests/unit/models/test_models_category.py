import pytest
from src.models import Category


@pytest.mark.django_db
class TestCategoryModel:
    def test_create_category(self, category: Category):
        assert category.name == "테스트 카테고리"
