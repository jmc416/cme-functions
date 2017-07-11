from datetime import datetime
import os

import requests

from azure.storage.file import FileService

ACCOUNT_NAME = os.environ.get('STORAGE_ACCOUNT_NAME')
KEY = os.environ.get('STORAGE_ACCOUNT_KEY')
SHARE_NAME = 'cme-reports'

RECEIPTS_DIRECTORY = 'delivery-receipts'
RECEIPTS_URL = ('http://www.cmegroup.com/delivery_reports/'
                'deliverable-commodities-under-registration.xls')
RECEIPTS_FILENAME_SUFFIX = '-deliverable-commodities-under-registration.xls'

STOCKS_DIRECTORY = 'stocks-of-grain'
STOCKS_URL = 'http://www.cmegroup.com/delivery_reports/stocks-of-grain-updated-tuesday.xls'
STOCKS_FILENAME_SUFFIX = '-stocks-of-grain-updated-tuesday.xls'

def filename(suffix):
    return datetime.now().strftime('%Y%m%d') + suffix


def get_bytes(url):
    return requests.get(url).content


f = FileService(account_name=ACCOUNT_NAME, account_key=KEY)
f.create_share(SHARE_NAME)

f.create_directory(SHARE_NAME, RECEIPTS_DIRECTORY)
f.create_file_from_bytes(SHARE_NAME, RECEIPTS_DIRECTORY,
                         filename(RECEIPTS_FILENAME_SUFFIX), get_bytes(RECEIPTS_URL))

f.create_directory(SHARE_NAME, STOCKS_DIRECTORY)
f.create_file_from_bytes(SHARE_NAME, STOCKS_DIRECTORY,
                         filename(STOCKS_FILENAME_SUFFIX), get_bytes(STOCKS_URL))



