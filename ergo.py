from pickle import FALSE
from xml.dom.minidom import TypeInfo
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


# Gets Ergo price from Coin Gecko
def GetCurrentPriceForErgo():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=usd"
    retries = 1
    success = False
    while not success:
        try:
            url_response = requests.get(url, timeout=10)
            data = json.loads(url_response.text)
            price = data['ergo']['usd']
            success = True
        except Exception as e:
            wait = retries * 10
            print('Error! Waiting %s secs and re-trying...' % wait)
            sys.stdout.flush()
            time.sleep(wait)
            if retries == 2:
                break
            retries += 1
    return price


# Gets Tokens for the Address and Gives Breakdown
def GetTokensFromAddress(address):
    url = "https://api.ergoplatform.com/api/v1/addresses/" + \
        str(address)+"/balance/confirmed"
    retries = 1
    success = False
    while not success:
        try:
            url_response = requests.get(url, timeout=10)
            data = json.loads(url_response.text)
        except Exception as e:
            wait = retries * 10
            print('Error! Waiting %s secs and re-trying...' % wait)
            sys.stdout.flush()
            time.sleep(wait)
            if retries == 2:
                break
            retries += 1

    nanoErgs = data['nanoErgs']
    tokenList = []
    for token in data['tokens']:
        tokenList.append(token['name'])
    return nanoErgs, tokenList


# data = GetTokensFromAddress(
#     "9h4XrgFbrHcZipDA6ziLtxAWxLHBS4KYYc3LBWM7JkFxHXj8geg")
# for token in data[1]:
#     print(token)
# print(type(data[1]))
