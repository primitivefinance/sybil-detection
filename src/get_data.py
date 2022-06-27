import requests
import pandas as pd
import os
from dotenv import load_dotenv


def get_data():
    load_dotenv()
    r = requests.get(
        "https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&sort=asc&apikey={}".format(
            os.environ["PRIMITIVE_MANAGER"], os.environ["ETHERSCAN_API"]
        )
    )
    a = r.json()
    df = pd.DataFrame(a["result"])
    users = df["from"]
    return users


def get_users_nieghbors(user):
    r = requests.get(
        "https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&sort=asc&apikey={}".format(
            user, os.environ["ETHERSCAN_API"]
        )
    )
    df = pd.DataFrame(r.json()["result"])
    df = df["to"].drop_duplicates()
    return df
