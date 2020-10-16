from django.core.validators import RegexValidator
from django.db.models import (
    TextChoices,
    JSONField,
    Model,
    CharField,
    BooleanField,
    EmailField,
    ForeignKey,
    SET,
    PositiveSmallIntegerField,
    DateTimeField,
    DateField,
)
from django.utils.translation import gettext_lazy as _


class Vendor(Model):
    """
    setup vendor in system
    """

    name = CharField(max_length=100, unique=True, null=True, blank=True)
    contact_name = CharField(max_length=100, null=True, blank=True)
    contact_phone = CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex="[0-9]{3}[-]{1}[0-9]{3}[-]{1}[0-9]{4}",
                message="Phone number format is 999-999-9999",
            )
        ],
    )
    # product = ManyToManyField(Vendor, through='Inventory',through_fields=('vendor','product')to_field="name")
    email = EmailField(max_length=254, unique=True)
    date_created = DateTimeField(auto_now=False, auto_now_add=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
