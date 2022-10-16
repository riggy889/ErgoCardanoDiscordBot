import logging
import requests
import json
import os
import cardano.cardanoApiFunctions as cardanoApi
from dotenv import load_dotenv

errorResponseString = "Error occurred, please contact Riggy for assistance"

logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s',
                    encoding='utf-8', level=logging.WARNING)


def CurrentFloorPrice(policyId):
    url = "https://api.opencnft.io/1/policy/" + \
        str(policyId)+"/floor_price"

    try:
        r = requests.get(
            url, headers={"accept": "application/json"}, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('Requests Exception Found')
        logging.warning(err)
        return errorResponseString

    data = json.loads(r.text)
    adaAmount = cardanoApi.lovelaceConverter(int(data['floor_price']))
    fpString = f"Current Floor Price is {adaAmount} ada"
    return fpString
