from maclookup import ApiClient
from io import open
import logging
import os

api_key = os.environ['API_KEY']
log_file = os.environ['LOG_FILENAME']
output_file = os.environ['OUTPUT_FILENAME']

client = ApiClient(api_key)

logging.basicConfig(filename=log_file, level=logging.WARNING)

csv_data = client.get_raw_data('08EA4026E5DE', 'csv')

f = open(output_file, 'w', encoding='utf-8')
f.write(csv_data)
