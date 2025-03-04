from typing import Sequence, Optional

from ...usecase._adaptor.product import ProductUseCaseAdaptor
from ...models.product import Product


class ProductServiceAdaptor(ProductUseCaseAdaptor):
    def get_product(self, product_idx: int) -> Product:
        return Product.objects.get(idx=product_idx)

    def get_products(self, category_idx: Optional[int] = None) -> Sequence[Product]:
        if category_idx is None:
            return Product.objects.all().select_related("category").order_by("-idx")
        return Product.objects.filter(category_id=category_idx).select_related("category").order_by("-idx")
