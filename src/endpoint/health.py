from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class HealthCheckView(APIView):
    @swagger_auto_schema(
        operation_description="Health Check API",
        responses={200: "pong"},
        tags=["health"],
    )
    def get(self, _):
        return Response("pong")
