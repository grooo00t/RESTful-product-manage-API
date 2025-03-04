from typing import Optional, Sequence

from ...usecase._adaptor.category import CategoryUseCaseAdaptor
from ...models.category import Category


class CategoryServiceAdaptor(CategoryUseCaseAdaptor):
    def get_categories(self) -> Sequence[Category]:
        return Category.objects.all()
