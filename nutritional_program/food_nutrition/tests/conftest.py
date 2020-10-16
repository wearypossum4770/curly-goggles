import pytest
from budget.models.vendors import Vendor


@pytest.fixture(scope="session")
@pytest.mark.django_db(transaction=True)
def create_test_vendor():
    new_vendor = {
        "name": "Django Admin 2",
        "contact_name": "Stephen Smith",
        "contact_phone": "123-456-7890",
        "is_active": True,
    }
    vendor = Vendor.objects.create(**new_vendor)
    print("I'm in config file")
    print("\n\n\n")
    print(vendor)
