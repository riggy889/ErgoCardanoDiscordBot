import requests
import json
import sys
import time
from retrying import retry

# api returns address of tokenID


def GetAddressByTokenID(tokenID):
    url = "https://api.ergoplatform.com/api/v1/boxes/unspent/byTokenId/"
    api_url = "https://api.ergoplatform.com/api/v1/boxes/unspent/byTokenId/"+tokenID

    retries = 1
    success = False
    while not success:
        try:
            url_response = requests.get(api_url, timeout=10)
            data = json.loads(url_response.text)
            address = data['items'][0]['address']
            success = True
        except Exception as e:
            wait = retries * 30
            print('Error! Waiting %s secs and re-trying...' % wait)
            sys.stdout.flush()
            time.sleep(wait)
            retries += 1
    return address


# tokenID = "b86b0b723c7dfc61f27c1f91c405413028d7c922e9ae1c00195eef3ecc03ee12"
# tokenID = "4578sadasd"
# address = GetAddressByTokenID(tokenID)
# print(address)
