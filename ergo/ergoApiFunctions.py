import requests
import json

import logging
logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s',
                    encoding='utf-8', level=logging.WARNING)

errorResponseString = "Error occurred, please contact Riggy for assistance"


# Gets Address By Token Id Provided
def GetAddressByTokenID(tokenID):
    url = "https://api.ergoplatform.com/api/v1/boxes/unspent/byTokenId/"+tokenID
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('Requests Exception Found')
        logging.warning(err)
        return errorResponseString

    data = json.loads(r.text)
    address = data['items'][0]['address']
    addressString = f"TokenID has been located in {address}"
    return addressString


# Gets Ergo price from Coin Gecko
def GetCurrentPriceForErgo():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=usd"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('Requests Exception Found')
        logging.warning(err)
        return errorResponseString

    data = json.loads(r.text)
    price = 'Current Ergo Price - $'+str(data['ergo']['usd'])

    return price


# Gets Erg Balance for the Address
def GetErgBalanceFromAddress(address):
    url = "https://api.ergoplatform.com/api/v1/addresses/" + \
        str(address)+"/balance/confirmed"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('Requests Exception Found')
        logging.warning(err)
        return errorResponseString

    nanoErgs = json.loads(r.text)['nanoErgs']
    ergAmount = str(round(nanoErgs / 1000000000, 2)) + ' ERG'
    return ergAmount


# Gets NFT Tokens for the Address
def GetTokensFromAddress(address):
    url = "https://api.ergoplatform.com/api/v1/addresses/" + \
        str(address)+"/balance/confirmed"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('Requests Exception Found')
        logging.warning(err)
        return errorResponseString

    tokens = json.loads(r.text)['tokens']
    tokenString = ""
    for token in tokens:
        tokenString += f"{str(token['name'])} (Qty - {str(token['amount'])}), \n"
    return tokenString


def GetTokenDetails(tokenID):
    # /api/v1/assets/search/byTokenId
    url = "https://api.ergoplatform.com/a/api/v1/assets/search/byTokenId/"+tokenID
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('Requests Exception Found')
        logging.warning(err)
        return errorResponseString

    data = json.loads(r.text)
    return data
