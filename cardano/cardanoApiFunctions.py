from blockfrost import BlockFrostApi, ApiError, ApiUrls
import logging
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BLOCKFROST_TOKEN')

logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s',
                    encoding='utf-8', level=logging.WARNING)

errorResponseString = "Error occurred, please contact Riggy for assistance"

api = BlockFrostApi(
    project_id=TOKEN,
    # base_url=ApiUrls.testnet.value,
    base_url=ApiUrls.mainnet.value,
)


def lovelaceConverter(lovelace):
    ada = round(int(lovelace) / 1000000, 2)
    return ada


def GetLastEpochRewards(stakeAddress):
    try:
        account_rewards = api.account_rewards(
            stake_address=str(stakeAddress),
            count=20,
            gather_pages=True,  # will collect all pages
        )
    except ApiError as e:
        print('Requests Exception Found')
        logging.warning(e)
        return errorResponseString

    rewards = lovelaceConverter(int(account_rewards[-1].amount))
    epoch = str(account_rewards[-1].epoch)
    rewardsString = f"Rewards Last Epoch ({epoch}) - {rewards} ada"
    return rewardsString
