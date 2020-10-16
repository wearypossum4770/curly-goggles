from django.db.models import (
    TextChoices,
    JSONField,
    Model,
    ForeignKey,
    CASCADE,
    SET,
    PositiveSmallIntegerField,
    DateTimeField,
    DateField,
)
from django.utils.translation import gettext_lazy as _
from .products import Product
from .vendors import Vendor


class Inventory(Model):
    product = ForeignKey(Product, on_delete=CASCADE, to_field="name")
    vendor = ForeignKey(Vendor, on_delete=CASCADE, to_field="name")
    # items = ForeignKey(Product, on_delete=CASCADE, related_name="")
    reorder_level = PositiveSmallIntegerField()
    reorder_quantity = PositiveSmallIntegerField()
    # vendor = ForeignKey('Vendor',to_field="name" on_delete=SET(self.set_date_deleted))
