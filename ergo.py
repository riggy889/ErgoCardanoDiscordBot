import requests
import json


# api returns address of tokenID
def GetAddressByTokenID(tokenID):
    url = "https://api.ergoplatform.com/api/v1/boxes/unspent/byTokenId/"
    api_url = "https://api.ergoplatform.com/api/v1/boxes/unspent/byTokenId/"+tokenID
    # try:
    #     url_response = requests.get(api_url, timeout=3)
    #     url_response.raise_for_status()
    # except requests.exceptions.HTTPError as errh:
    #     return "An Http Error occurred:" + repr(errh)
    # except requests.exceptions.ConnectionError as errc:
    #     return "An Error Connecting to the API occurred:" + repr(errc)
    # except requests.exceptions.Timeout as errt:
    #     return "A Timeout Error occurred:" + repr(errt)
    # except requests.exceptions.RequestException as err:
    #     return "An Unknown Error occurred" + repr(err)
    url_response = requests.get(api_url, timeout=3)
    url_response.raise_for_status()

    data = json.loads(url_response.text)
    address = data['items'][0]['address']
    return address


# tokenID = "b86b0b723c7dfc61f27c1f91c405413028d7c922e9ae1c00195eef3ecc03ee12"
# address = GetAddressByTokenID(tokenID)
# print(address)
