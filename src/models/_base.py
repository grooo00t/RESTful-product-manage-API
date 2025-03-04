from django.db import models
from datetime import datetime


class _BaseModel(models.Model):
    """
    _BaseModel 모델:

    - idx: 고유 식별자 (자동 증가 필드)
    - created_at: 생성 시간 (자동 생성)
    - updated_at: 수정 시간 (자동 업데이트)
    """

    idx: int = models.AutoField(primary_key=True)
    created_at: datetime = models.DateTimeField(auto_now_add=True, null=True)
    updated_at: datetime = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
