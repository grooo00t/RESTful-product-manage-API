import abc
from typing import Sequence

from ..models.category import Category
from ._adaptor.category import CategoryUseCaseAdaptor


class GetCategoriesUseCase(metaclass=abc.ABCMeta):
    def __init__(self, category_adaptor: CategoryUseCaseAdaptor):
        self.category_adaptor = category_adaptor

    def execute(self) -> Sequence[Category]:
        return self.category_adaptor.get_categories()
