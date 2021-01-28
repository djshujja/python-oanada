import requests
import  json

from requests.models import Response
import  numpy as np
import pandas as pd
import time


API = "api-fxpractice.oanda.com"
STR_API = "stream-fxpractice.oanda.com"

ACCESS_TOKEN = '58bbfd0542135613ab6efb2f1a9d133b-1f580cfa7d4b1dd159f5af7b48ce8f36'

ID = "101-004-4838689-002"


def simple():
    # path = f"/v3/accounts/{ID}/pricing"
    path = f"/v3/accounts/{ID}"
    query = {"instruments":"GBP_USD"}
    headers = {"Authorization": "Bearer 58bbfd0542135613ab6efb2f1a9d133b-1f580cfa7d4b1dd159f5af7b48ce8f36"}
    # response = requests.get("https://"+ API + path, headers=headers, params=query)


    response = requests.get("https://"+ API + path, headers=headers, params=query)

    # response.json()
    print(response.json())

from_time = time.mktime(pd.to_datetime("01/20/2021").timetuple())
to_time = time.mktime(pd.to_datetime("01/26/2021").timetuple())
print(f"Window Start: {from_time}, Window End:{to_time}.")


headers = {"Authorization": "Bearer 58bbfd0542135613ab6efb2f1a9d133b-1f580cfa7d4b1dd159f5af7b48ce8f36"}
query = {"from" : str(from_time), "to":str(to_time), "granularity":"D"}

INSTRUMENT = "GBP_USD"

CANDLES_PATH= f"/v3/accounts/{ID}/instruments/{INSTRUMENT}/candles"
response = requests.get("https://"+ API + CANDLES_PATH, headers=headers, params=query)


def json_to_pandas(json):
    json_file = json
    price_json = json_file["candles"]
    times =[]
    close_price, high_price,low_price,open_price = [],[],[],[]

    for candle in price_json:
        times.append(candle["time"])
        close_price.append(float(candle["mid"]["c"]))
        high_price.append(float(candle["mid"]["h"]))
        low_price.append(float(candle["mid"]["l"]))
        open_price.append(float(candle["mid"]["o"]))

    dataframe = pd.DataFrame({"close":close_price, "high":high_price, "low":low_price, "open":open_price})
    dataframe.index = pd.to_datetime(times)
    return dataframe

GBPJPY_df = json_to_pandas(response.json())
print(GBPJPY_df.head())

# GBPJPY_df["close"].plot()

# respone = STR_API.pricing.stream(accountID=ID, instruments="GBP_USD", snapshot=true)
# response = requests.get("https://"+ STR_API + CANDLES_PATH, headers=headers, params=query)




# print(response.json())
# for x in response.lines:
#     print(x)



















