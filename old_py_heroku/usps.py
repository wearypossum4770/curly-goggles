import requests
mailing_address_1 = "SUITE K"
mailing_address_2 = "29851 Aventura"
mailing_state = "CA"
mailing_zip5 = "92688"
USPS_SHIPPING_API_COMPANY="dragoomdoc"
USPS_SHIPPING_API_USERNAME="348DRAGO5925"
USPS_SHIPPING_API_PASSWORD="722XO92WE592"
# ~ <?xml version="1.0" encoding="UTF-8"?>

xml_data = f"""
	<AddressValidateRequest USERID={USPS_SHIPPING_API_USERNAME}>

	<Revision>1</Revision>

	<Address ID="0">

	<Address1>{mailing_address_1}</Address1>

	<Address2>{mailing_address_2}</Address2>

	<City/>

	<State>{mailing_state}</State>

	<Zip5>{mailing_zip5}</Zip5>

	<Zip4/>

	</Address>

	</AddressValidateRequest>
"""
def validate_us_address():
	url = f"http://production.shippingapis.com/ShippingAPI.dll?API=Verify&XML={xml_data}"
	headers = {'Content-Type': 'application/xml'} # set what your server accepts
	resp = requests.get(url, data=xml_data, headers=headers)
	return resp

print(validate_us_address())
