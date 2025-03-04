from rest_framework.request import Request
from django.http.response import JsonResponse

from ..exception import _BaseError


class ResponseHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request):
        return self.get_response(request)

    def process_exception(self, _: Request, exception: Exception):
        if isinstance(exception, _BaseError):
            return JsonResponse(
                {"code": exception.code(), "message": exception.message()},
                status=exception.status_code(),
            )
        return None
