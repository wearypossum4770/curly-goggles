from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# ~ def validate_phone_number(phone_number):
	# ~ phone_number_regex = '[0-9]{3}[-]{1}[0-9]{3}[-]{1}[0-9]{4}'
	# ~ RegexValidator = (
		# ~ regex = phone_number_regex, 
		# ~ message = "Enter a valid US phone number format: xxx-xxx-xxxx"
		
		# ~ )
def validate_us_address():
	
	xml = """
		<?xml version="1.0" encoding="UTF-8"?>
			<AddressValidateRequest USERID={settings.USPS_SHIPPING_API_USERNAME}>

				<Revision>1</Revision>

				<Address ID="0">

				<Address1>SUITE K</Address1>

				<Address2>29851 Aventura</Address2>

				<City/>

				<State>CA</State>

				<Zip5>92688</Zip5>

				<Zip4/>

				</Address>

			</AddressValidateRequest>
	"""
	
	url = f"https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&XML={xml}"
	return xml
	headers = {'Content-Type': 'application/xml'} # set what your server accepts
	response = requests.get(url, data=xml, headers=headers).text
print(validate_us_address())
