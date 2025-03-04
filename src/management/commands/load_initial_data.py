from django.core.management.base import BaseCommand
from django.core.management import call_command
from ...models import Category, Product, Coupon


class Command(BaseCommand):
    help = "Load initial data if tables are empty"

    def handle(self, *args, **options):
        if not Category.objects.exists():
            self.stdout.write("Loading categories...")
            call_command("loaddata", "categories")
            self.stdout.write(self.style.SUCCESS("Categories loaded successfully"))

        if not Product.objects.exists():
            self.stdout.write("Loading products...")
            call_command("loaddata", "products")
            self.stdout.write(self.style.SUCCESS("Products loaded successfully"))

        if not Coupon.objects.exists():
            self.stdout.write("Loading coupons...")
            call_command("loaddata", "coupons")
            self.stdout.write(self.style.SUCCESS("Coupons loaded successfully"))
