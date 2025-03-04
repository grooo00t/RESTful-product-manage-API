"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .settings import DEBUG

from ..endpoint.category import CategoryManageView
from ..endpoint.product import ProductManageView, ProductDetailManageView
from ..endpoint.health import HealthCheckView
from ..views.product import product_list, product_detail


schema_view = get_schema_view(
    openapi.Info(
        title="API 문서",
        default_version="v1",
        description="RESTful Shopping Mall Product Management API",
        contact=openapi.Contact(email="thschsmd@naver.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = []

# Template Views
urlpatterns += [
    path("products/", product_list, name="product-list-ui"),
    path("products/<int:product_idx>/", product_detail, name="product-detail-ui"),
]

# Api
api_urlpatterns = [
    # Health Check
    path("ping/", HealthCheckView.as_view(), name="health-check"),
    # Swagger
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Category
    path("categories/", CategoryManageView.as_view(), name="category"),
    # Product
    path("products/", ProductManageView.as_view(), name="product"),
    path("products/<int:product_idx>/", ProductDetailManageView.as_view(), name="product-detail"),
]

# API URLs
urlpatterns += [
    path("api/", include(api_urlpatterns)),
]

# Admin URLs (only in DEBUG mode)
if DEBUG:
    urlpatterns += [path("admin/", admin.site.urls)]
