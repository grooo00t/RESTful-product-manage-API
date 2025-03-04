from django.contrib import admin
from .models import Product, Category, Coupon


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "discount_rate", "coupon_applicable"]
    list_filter = ["category", "coupon_applicable"]
    search_fields = ["name", "description"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ["code", "discount_rate"]
    search_fields = ["code"]
