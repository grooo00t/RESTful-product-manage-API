import abc
from typing import Sequence

from ...models.category import Category


class CategoryUseCaseAdaptor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_categories(self) -> Sequence[Category]: ...
