from django.db.models import (
    Model,
    PositiveSmallIntegerField,
    DateTimeField,
    CharField,
    SET,
    CASCADE,
    DecimalField,
    ForeignKey,
)
from django.utils.translation import gettext_lazy as _
from .vendors import Vendor

# class OrderDetails(Model):
#     order = ForeignKey()
#     product = ForeignKey()
#     quantity = PositiveSmallIntegerField()


class Order(Model):
    vendor = ForeignKey(Vendor, on_delete=CASCADE)
    date_deleted = DateTimeField()
    total = DecimalField(max_digits=7, decimal_places=2)
    # details = ForeignKey(OrderDetails, on_delete=SET(self.set_date_deleted))

    def set_date_deleted(self):
        deleted = Order.objects.get_or_create(
            date_deleted=datetime.now(), deleted_by=User.username
        )
        deleted.save()

    def get_queryset(self):
        """
        Check user role, I will have admin access she will be staff.
        Others will be regular users. Prevents accidental deletions.
        """
        orders = (
            Order.objects.all()
            if self.request.user.is_admin
            else Order.objects.all().filter(date_deleted)
        )
        return orders
