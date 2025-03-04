from typing import Optional

from ._adpator.category import CategoryServiceAdaptor
from ..usecase._adaptor.category import CategoryUseCaseAdaptor
from ..usecase.category import GetCategoriesUseCase


class GetCategoriesService(GetCategoriesUseCase):
    def __init__(self, category_service_adaptor: Optional[CategoryUseCaseAdaptor] = None):
        super().__init__(category_service_adaptor or CategoryServiceAdaptor())
