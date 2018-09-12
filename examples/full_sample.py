from maclookup import ApiClient
import logging
import os

api_key = os.environ['API_KEY']
log_file = os.environ['LOG_FILENAME']


client = ApiClient(api_key)

logging.basicConfig(filename=log_file, level=logging.WARNING)

print(client.get_raw_data('08EA4026E5DE', 'csv'))
print(client.get_vendor('08EA4026E5DE'))

response = client.get('08EA4026E5DE')
print(response.vendor_details.is_private)
print(response.block_details.block_size)
