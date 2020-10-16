from django.db.models import (
    TextChoices,
    JSONField,
    Model,
    ManyToManyField,
    SET,
    CharField,
    DecimalField,
    ImageField,
    PositiveSmallIntegerField,
    DateTimeField,
    DateField,
)
from django.utils.translation import gettext_lazy as _


def additional_information():
    add_info = {}
    return add_info


def get_or_create_product_img():
    pass


def get_or_create_internal_barcode():
    pass


def get_or_create_external_barcode():
    pass


class Product(Model):
    class Category(TextChoices):
        ANIMAL_PROTEIN = "AP"
        PLANT_PROTEIN = "PP"
        DAIRY = "DA"
        FAT = "FT"
        DESSERT = "DE"
        BEVERAGE = "BB"
        GRAINS = "GR"
        FRUIT = "FR"
        VEGGIES = "VG"

    class Storage(TextChoices):
        KEEP_FROZEN = "ZERO", _("")
        REFRIGERATION_NEEDED = "COLD", _("")
        DRY_STORAGE = "DRY", _("")
        __empty__ = _("(Unknown)")

    name = CharField(max_length=100, unique=True)
    price = DecimalField(max_digits=7, decimal_places=2)
    description = CharField(max_length=200)
    item_size = PositiveSmallIntegerField()
    information = JSONField("Additional Information", default=additional_information)
    storage_method = CharField(
        max_length=4, choices=Storage.choices, default=Storage.__empty__
    )
    external_barcode = ImageField(get_or_create_external_barcode)
    internal_barcode = ImageField(default=get_or_create_internal_barcode)
    img = ImageField(default=get_or_create_product_img)
    date_created = DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.name} {self.price}"

    def set_date_deleted(self):
        from datetime import datetime

        return datetime.now()

    def get_barode(self):
        import barcode
        from barcode.writter import ImageWriter
