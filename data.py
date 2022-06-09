"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: IvetteLandaverde                                                                      -- #
# -- license:                                                -- #
# -- repository: https://github.com/IvetteLandaverde/Laboratorio-1                                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# ------- ORDER BOOKS -------- #

#dict_test = {'key_a': 'a', 'key_b': 'b'}
import numpy as np
import pandas as pd
import json

# Opening JSON file
#f= open("orderbooks_05jul21.json")
f=open('/Users/ivettelandaverde/Desktop/MyST/lab1/Laboratorio-1/orderbooks_05jul21.json')

# Returns JSON object as a dictionary
orderbooks_data = json.load(f)
ob_data = orderbooks_data["bitfinex"]

# Drop None keys
ob_data={i_key: i_value for i_key, i_value in ob_data.items() if i_value is not None}

# Convert to dataframe and rearange columns 
ob_data = {i_ob: pd.DataFrame(ob_data[i_ob])[["bid_size","bid","ask","ask_size"]] 
           if ob_data[i_ob] is not None else None for i_ob in list(ob_data.keys())}

# for largo 
i_count=0
l_data=[]
for i_data in ob_data.values():
    #i_data=list(ob_data.values())[0].vales()
    i_count += 1
    if i_data is None:
        print(i_data)
        l_data.append(i_count)

ob_data
# ------- PUBLIC TRADES -------- #

# Read csv
pt_data2=pd.read_csv("/Users/ivettelandaverde/Desktop/MyST/lab1/Laboratorio-1/btcusdt_binance.csv")
pt_data=pd.read_csv("/Users/ivettelandaverde/Desktop/MyST/lab1/Laboratorio-1/btcusdt_binance.csv")
#dtype=dtypes

#pt_data.drop(pt_data.columns[[0]],axis=1,inplace=True)
#pt_data2.drop(pt_data2.columns[[0]],axis=1,inplace=True)
