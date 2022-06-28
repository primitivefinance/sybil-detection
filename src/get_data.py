import requests
import pandas as pd
import os
from dotenv import load_dotenv


def get_data():
    load_dotenv()
    r = requests.get(
        "https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}".format(
            os.environ["CONTRACT_TO_LOOK_AT"], os.environ["ETHERSCAN_API"]
        )
    )
    a = r.json()
    df = pd.DataFrame(a["result"])
    return df.drop_duplicates()
