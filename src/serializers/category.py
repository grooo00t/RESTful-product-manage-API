from rest_framework import serializers
from ..models.category import Category
from ..utils.http.response import response_to_serializer


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["idx", "name"]


GetCategoriesResponseSerializer = response_to_serializer(GetCategorySerializer(many=True))
