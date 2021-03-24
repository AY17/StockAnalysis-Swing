import requests
#import pandas as pd 
#import numpy as np 
import json

def connection():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36',
           'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
           res = requests.get("https://www.nseindia.com/", headers=headers,timeout=5)
           cookies=res.cookies
           response=requests.get("https://www.nseindia.com/api/corporates-pit?index=equities&from_date=23-03-2021&to_date=24-03-2021",headers=headers,cookies=cookies,timeout=5)
