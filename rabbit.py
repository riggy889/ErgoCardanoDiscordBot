import requests
import json
import sched, time
import logging
logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s',
                    encoding='utf-8', level=logging.WARNING)
errorResponseString = "Error occurred, please contact Riggy for assistance"

def GetLatestRabbitSales():
    # rabbit image url = "https://image-optimizer.jpgstoreapis.com/QmRp67NMoJ4AhH1id91jrzApE9k2P3Daoryreb6nh1bQhh"
    url = "https://server.jpgstoreapis.com/collection/de2340edc45629456bf695200e8ea32f948a653b21ada10bc6f0c554/transactions?page=1&count=10&traits=%7B%7D&name="
    # url = "https://server.jpgstoreapis.com/collection/f4873b426a498350c579690bd1f4a369d5d7b521c778acf322f77334/transactions?page=1&count=10&traits=%7B%7D&name="

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException as err:
        print('Requests Exception Found')
        logging.warning(err)
        return errorResponseString

    data = json.loads(r.text)
    return data['transactions']


def build_rabbit_string(rabbitData):
    rabbitName = str(rabbitData['display_name'])
    rabbitSalePrice = str(rabbitData['amount_lovelace'])
    # rabbitRecentTxn = str(rabbitData['tx_hash'])
    rabbitString = f'{rabbitName} sold for {rabbitSalePrice}'
    # print(rabbitString)
    return rabbitString

def BuildExistingTxnList(rabbitData):
    txnList = []
    for rabbit in rabbitData:
        txnList.append(rabbit['tx_hash'])
    return txnList
