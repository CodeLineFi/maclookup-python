from maclookup import *
from maclookup.models import *
from maclookup.exceptions import EmptyResponseException
from .mock_requester import MockRequester
import unittest
from dateutil.parser import parse


class ApiClientTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_parsing(self):
        payload = """{
    "vendorDetails":
    {         
        "oui": "B0ECA1",
        "isPrivate": 0,
        "companyName": "CISCO",
        "companyAddress": "",  
        "countryCode": "US"  
    },
    "blockDetails": 
    {
        "blockFound": 1, 
        "borderLeft": "B0ECA1B0ECA1", 
        "borderRight": "B0ECE1B0ECA1",
        "blockSize": 32000, 
        "assignmentBlockSize": "MA-M", 
        "dateCreated": "26-09-1999",
        "dateUpdated": "26-09-2017"
    },
    "macAddressDetails":
    {
        "searchTerm": "B0ECE1B0ECA1", 
        "isValid": 1, 
        "transmissionType": "multicast", 
        "administrationType": "UAA" 
    }
}"""
        fake_requester = MockRequester(payload)

        client = ApiClient('test')
        client.set_requester(fake_requester)

        valid_object = ResponseModel()
        valid_object.vendor_details = VendorDetails()
        valid_object.vendor_details.oui = "B0ECA1"
        valid_object.vendor_details.is_private = 0
        valid_object.vendor_details.company_name = "CISCO"
        valid_object.vendor_details.company_address = ""
        valid_object.vendor_details.country_code = "US"
        valid_object.block_details = BlockDetails()
        valid_object.block_details.block_found = 1
        valid_object.block_details.border_left = "B0ECA1B0ECA1"
        valid_object.block_details.border_right = "B0ECE1B0ECA1"
        valid_object.block_details.block_size = 32000
        valid_object.block_details.assignment_block_size = "MA-M"
        valid_object.block_details.date_created = parse("26-09-1999")
        valid_object.block_details.date_updated = parse("26-09-2017")
        valid_object.mac_address_details = MacAddressDetails()
        valid_object.mac_address_details.search_term = "B0ECE1B0ECA1"
        valid_object.mac_address_details.is_valid = 1
        valid_object.mac_address_details.transmission_type = "multicast"
        valid_object.mac_address_details.administration_type = "UAA"

        self.assertEqual(client.get('MAC'), valid_object)

    def test_vendor_name(self):
        payload = "Test Company Name, Inc."

        fake_requester = MockRequester(payload)

        client = ApiClient('test')
        client.set_requester(fake_requester)

        self.assertEqual(client.get_vendor("MAC"), payload)

    def test_raw_data(self):
        payload = """<Response>
    <vendorDetails>
        <oui>F40F24</oui>
        <isPrivate>false</isPrivate>
        <companyName>Apple, Inc</companyName>
        <companyAddress>1 Infinite Loop Cupertino  CA  95014 US</companyAddress>
        <countryCode>US</countryCode>
    </vendorDetails>
    <blockDetails>
        <blockFound>true</blockFound>
        <borderLeft>F40F240000000000</borderLeft>
        <borderRight>F40F24FFFFFFFFFF</borderRight>
        <blockSize>1099511627776</blockSize>
        <assignmentBlockSize>MA-L</assignmentBlockSize>
        <dateCreated></dateCreated>
        <dateUpdated></dateUpdated>
    </blockDetails>
    <macAddressDetails>
        <searchTerm>F40F2436DA57</searchTerm>
        <isValid>true</isValid>
        <transmissionType>multicast</transmissionType>
        <administrationType>LAA</administrationType>
    </macAddressDetails>
</Response><Response>
    <vendorDetails>
        <oui>F40F24</oui>
        <isPrivate>false</isPrivate>
        <companyName>Apple, Inc</companyName>
        <companyAddress>1 Infinite Loop Cupertino  CA  95014 US</companyAddress>
        <countryCode>US</countryCode>
    </vendorDetails>
    <blockDetails>
        <blockFound>true</blockFound>
        <borderLeft>F40F240000000000</borderLeft>
        <borderRight>F40F24FFFFFFFFFF</borderRight>
        <blockSize>1099511627776</blockSize>
        <assignmentBlockSize>MA-L</assignmentBlockSize>
        <dateCreated></dateCreated>
        <dateUpdated></dateUpdated>
    </blockDetails>
    <macAddressDetails>
        <searchTerm>F40F2436DA57</searchTerm>
        <isValid>true</isValid>
        <transmissionType>multicast</transmissionType>
        <administrationType>LAA</administrationType>
    </macAddressDetails>
</Response>"""

        fake_requester = MockRequester(payload)

        client = ApiClient('test')
        client.set_requester(fake_requester)

        self.assertEqual(client.get_raw_data("MAC", "xml"), payload)

    def test_get_empty_response(self):
        payload = ""
        fake_requester = MockRequester(payload)

        client = ApiClient('test')
        client.set_requester(fake_requester)

        with self.assertRaises(EmptyResponseException):
            client.get("MAC")

    def test_get_raw_data_empty_response(self):
        payload = ""
        fake_requester = MockRequester(payload)

        client = ApiClient('test')
        client.set_requester(fake_requester)

        with self.assertRaises(EmptyResponseException):
            client.get_raw_data("MAC", "xml")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
