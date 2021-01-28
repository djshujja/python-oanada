from main import ACCESS_TOKEN
import pandas as pd 
import oandapyV20 
from oandapyV20.endpoints import pricing
import configparser

accountID = '101-004-4838689-002'
ACCESS_TOKEN = '58bbfd0542135613ab6efb2f1a9d133b-1f580cfa7d4b1dd159f5af7b48ce8f36'

api = API(access_token=ACCESS_TOKEN)
params = {
    "instruments":"EUR_USD"
}
r = pricing.PricingInfo(accountID=accountID, params=params)
rv = api.request(r)
print(r.json())

'''
Oxiliary Learning
Bloom Berg

'''