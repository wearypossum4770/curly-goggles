from django.db.models import (
Model, PositiveIntegerField, CharField
)

# Create your models here.
class Address(Model):
	mailing_street_1 = CharField(max_length=100)
	mailing_street_2 = CharField(max_length=100, null=True)
	mailing_city = CharField(max_length=100)
	mailing_state =CharField(max_length=2,null=True)
	mailing_zip5 =PositiveIntegerField(null=True)
	mailing_zip4 = PositiveIntegerField(null=True)
	
	def validate_address(self, request):
		import requests
			
		xml = f'<?xml version="1.0" encoding="UTF-8"?><AddressValidateRequest USERID={settings.USPS_SHIPPING_API_USERNAME}><Revision>1</Revision><Address ID="0"><Address1>{self.mailing_street_2}</Address1><Address2>{self.mailing_street_2}</Address2><City>{self.mailing_city}</City><State>{self.mailing_state}</State><Zip5>{self.mailing_zip5}</Zip5><Zip4/></Address></AddressValidateRequest>'
		url = f"https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&XML={xml}"
		headers = {'Content-Type': 'application/xml'} # set what your server accepts
		resp = requests.get(url, data=xml, headers=headers).text
		print(resp)


test_address = {
"mailing_street_1":"1600 Pennsylvania Ave Nw",
"mailing_city":"Washington",
"mailing_state":"DC" ,
"mailing_zip5":"20500",
}
