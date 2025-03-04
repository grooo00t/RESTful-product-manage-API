import abc
from typing import Sequence, Optional

from ...models.product import Product


class ProductUseCaseAdaptor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_product(self, product_idx: int) -> Product: ...

    @abc.abstractmethod
    def get_products(self, category_idx: Optional[int] = None) -> Sequence[Product]: ...
