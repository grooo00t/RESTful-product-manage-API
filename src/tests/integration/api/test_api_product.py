import pytest
from rest_framework import status
from src.models import Product


@pytest.mark.django_db
class TestProductAPI:
    base_url = "/api/products"

    def test_list_products_empty(self, api_client):
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["data"]["results"]) == 0

    def test_list_products_with_data(self, api_client, product: Product):
        response = api_client.get(f"{self.base_url}/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["data"]["results"]) == 1
        assert response.data["data"]["results"][0]["name"] == product.name

    def test_retrieve_product(self, api_client, product: Product):
        response = api_client.get(f"{self.base_url}/{product.idx}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["data"]["name"] == product.name

    def test_retrieve_product_not_found(self, api_client):
        response = api_client.get(f"{self.base_url}/1/")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["code"] == "PRODUCT_0001"

    def test_list_products_with_category_filter(self, api_client, product: Product):
        response = api_client.get(f"{self.base_url}/", {"category_idx": product.category.idx})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["data"]["results"]) == 1
        assert response.data["data"]["results"][0]["category"]["idx"] == product.category.idx
