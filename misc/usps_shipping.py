import json
from requests_xml import XML, XMLSession

dragoomdoc = {
    "username": "693DRAGO4853",
    "password": "536ES52JZ916",
}

ADDRESS1 = "SUITE K"
ADDRESS2 = "29851 Aventura"
STATE = "CA"
ZIP5 = "92688"


class ShippingValidator:
    def __init__(self):
        self.session = XMLSession()

    def receive_address_data():
        pass


def send_addresss_data():
    session = XMLSession()
    xml_data = f"""
<employees>
    <person>
        <name value="Alice"/>
	</person>
    <person>
        <name value="{dragoomdoc['username']}"/>
    </person>
</employees>
"""

    usps_api_signature = (
        f"https://secure.shippingapis.com/ShippingAPI.dll?API=Verify&XML={xml_data}"
    )

    xml_document = XML(xml=xml_data)
    print(usps_api_signature)
    return xml_document.json()


print(send_addresss_data())
