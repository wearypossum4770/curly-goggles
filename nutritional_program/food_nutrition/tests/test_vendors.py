from unittest import main
from django.test import TestCase
import pytest

from budget.models.vendors import Vendor
from budget.models.products import Product

@pytest.mark.django_db
node_uuid = {
	1: "099d7dc0-f2ff-11ea-857b-a391799fa2a0",
	4:"263a3673-758a-4caa-9a28-f8bfbbca2532",
}
# idempotency_key = 
calories=160, total_fat=8, sat_fat=4.5, trans_fat=0, cholesterol=30, sodium=85, total_carb = 11, fiber=0, total_sugar=10, added_sugar=0, protein=8, vitamin_d = 10, calcium=25, iron=0, potassium=8, 

class TestVendor(TestCase):
    pytestmark = pytest.mark.django_db
    # @pytest.mark.django_db(transaction=True)
    def setUp(self):
        new_vendor = Vendor.objects.create(
            name="Django Admin 2",
            contact_name="Stephen Smith",
            contact_phone="123-456-7890",
            is_active=True,
        )
        product_image = "/home/gatorcollege2006/web_dev/nutritional_program/food_nutrition/private/images/.tests/great_value_milk_gallon.jpeg"

        # new_product = Product.objects.create(name="", price= 3.10, description='', item_size=128,information='', storage_method=Product.Storage.REFRIGERATION_NEEDED, external_barcode='', internal_barcode='', img=product_image)
        # self.product = Product.objects.get(pk=1)
        self.vendor = Vendor.objects.get(pk=1)

    def test_vendor_exists(self):
        self.assertIsNotNone(self.vendor)

    def test_class_instance(self):
        self.assertIsInstance(self.vendor, Vendor)

    def test_vendor_name(self):
        self.assertTrue(self.vendor.name, "Django Admin 2")


if __name__ == "__main__":
    main(verbosity=2, failfast=True)
