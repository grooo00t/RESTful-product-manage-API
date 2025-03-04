from django.db import models

from ._base import _BaseModel


class Category(_BaseModel):
    """
    Category 모델:

    - name: 카테고리 이름 (문자열, 최대 100자)
    """

    name: str = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "category"
