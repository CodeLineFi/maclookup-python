========
Overview
========

Client library for `macaddress.io <https://macaddress.io>`_ on Python
language.

* Free software: MIT

Installation
============
::

    pip install maclookup

or

::

    git clone https://github.com/CodeLineFi/maclookup-python.git
    pip install -e /path_to_sdist/

or

::

    cd /path_to_sdist/
    python setup.py install

or

::

    cd /path_to_sdist/
    easy_install .

Sample code
===========
::

    from maclookup import ApiClient
    import logging

    client = ApiClient('Your API key')

    logging.basicConfig(filename='myapp.log', level=logging.WARNING)

    print(client.get_raw_data('00A043AAAAAA', 'json'))
    print(client.get_vendor('BBA043AAAAAA'))
    print(client.get('BBA043AAAAAA'))

    response = client.get('00A043AAAAAA')
    print(response.vendor_details.is_private)
    print(response.block_details.date_created)


Examples
========

You may find some examples in the "examples" directory. To run these
examples you need to install "maclookup" package. Then you need to create an
account on `macaddress.io <https://macaddress.io>`_. The last step is
defining environment variables with the value of your API key and other
settings.

::

    export API_KEY=<Your API key>
    export LOG_FILENAME=myapp.log
    export OUTPUT_FILENAME=result.csv

Documentation
=============

maclookup package contains the API client class **ApiClient** which
implements the following functionality

ApiClient methods list:

1. get(mac): ResponseModel
    Returns ResponseModel object as a parsed API response for a given MAC address
    or OUI

2. get_vendor(mac): string
    Returns the company name as text

3. get_raw_data(mac, output_format): string
    Returns non-parsed API response as string

4. set_base_url(url)
    Sets base url to *url*

5. set_requester(requester)
    Sets instance of Requester

ResponseModel fields:

1. vendor_details: VendorDetails
2. block_details: BlockDetails
3. mac_address_details: MacAddressDetails

VendorDetails fields:

1. oui: string
2. is_private: boolean (False|True)
3. company_name: string
4. company_address: string
5. country_code: string

BlockDetails fields:

1. block_found: boolean (False|True)
2. border_left: string (MAC address, may be in the EUI-64)
3. border_right: string (MAC address, may be in the EUI-64)
4. block_size: int (long long int)
5. assignment_block_size: string
6. date_created: instance of datetime.datetime
7. date_updated: instance of datetime.datetime

MacAddressDetails fields:

1. search_term: string
2. is_valid: boolean (False|True)
3. transmission_type: string
4. administration_type: string

If the server returns marker of outdated API version, this library will
write a warning to a log.


Development
===========

To install dev requirements, you need to run following commands:

::

    cd /path_to_sdist/
    pip install -e .[dev]

To run unit tests, you may use the following command:

::

    cd /path_to_sdist/
    python -m unittest discover . "*_test.py"

or this one

::

    cd /path_to_sdist/
    tox
