from django.db import models

# Create your models here.

rents
royalties
other_income
federal_income_tax_withheld
fishing_boat_proceeds
medical_and_health_care_payments
direct_sales_for_resale = BooleanField(help_text="Payer made direct sales of $5,000 or more of consumer products to a buyer (recipient) for resale")
substitute_payments (help_text="substitute payments in lieu of dividends or interest")


class Tax:
	class Type:
		FUTA
		SUTA
		OASDI
		SOCIAL_SECURITY
		HI
