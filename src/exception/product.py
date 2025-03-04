from ..exception import _BaseError


class ProductNotFoundError(_BaseError):
    @classmethod
    def status_code(cls) -> int:
        return 404

    @classmethod
    def code(cls) -> str:
        return "PRODUCT_0001"

    @classmethod
    def message(cls) -> str:
        return "상품을 찾을 수 없습니다."
