import pytest
from rest_framework import status
from src.models import Product


@pytest.mark.django_db
class TestProductAPI:
    def test_list_products(self, api_client, product: Product):
        response = api_client.get("/api/products/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["data"]["results"]) == 1

    def test_retrieve_product(self, api_client, product: Product):
        response = api_client.get(f"/api/products/{product.idx}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["data"]["name"] == product.name

    def test_retrieve_product_not_found(self, api_client, product: Product):
        response = api_client.get(f"/api/products/{product.idx+1}/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["code"] == "PRODUCT_0001"
