from django.db.models import (
    Models,
    CharField,
)

# Create your models here.
class Organization(Model):
    legal_name = CharField(max_length=50)
    # depatment = selection
    # fax_number = CharField(max_length=10)
    # has_credential = #???? permissions?
    # interaction_statistics= # ??? Some math stuff here
    # organization_logo_seal = ImageField()
    # location
    # members =
    is_non_profit = BooelanFiled(default=False)


class OrganizationMembers(Model):
    # UserAccount
    organization_name = CharField(max_length=50)
